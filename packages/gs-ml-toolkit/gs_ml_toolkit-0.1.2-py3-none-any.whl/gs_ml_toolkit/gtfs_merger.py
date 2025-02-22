"""
GTFSProcessor module

This module provides the GTFSProcessor class to load and merge GTFS data.
"""

import os
import glob
import shutil
from datetime import datetime
import pandas as pd

class GTFSProcessor:
    """
    A class used to process GTFS data.

    This class contains methods to load partitions from a PartitionedDataset
    and merge GTFS folders, deduplicate and join data from various GTFS files.

    Attributes
    ----------
    None

    Methods
    -------
    load_partitions(gtfs)
        Loads partitions from a PartitionedDataset and returns a dictionary of DataFrames.
    merge_gtfs_folders(gtfs_input)
        Merges GTFS data from a partitioned dataset or a single DataFrame and returns
        a unified DataFrame with stops information.
    """

    @staticmethod
    def load_partitions(gtfs):
        """
        Loads partitions from a PartitionedDataset and returns a dictionary with DataFrames.

        Parameters
        ----------
        gtfs : dict or pd.DataFrame
            A dictionary where keys are partition names and values are callable methods that return DataFrames.
            If already a DataFrame, it is returned as is.

        Returns
        -------
        dict or pd.DataFrame
            A dictionary mapping partition names to DataFrames, or the original DataFrame.
        """
        if not isinstance(gtfs, pd.DataFrame):
            dataframes = {}
            for partition_name, dataset_method in gtfs.items():
                print(f"Processing partition: {partition_name}")
                df = dataset_method()  # Obtain the DataFrame from the callable
                dataframes[partition_name] = df
            return dataframes
        else:
            return gtfs

    @staticmethod
    def merge_gtfs_folders(gtfs_input):
        """
        Merges GTFS data from either a partitioned dataset or a single DataFrame.

        Parameters
        ----------
        gtfs_input : dict or pd.DataFrame
            Either a partitioned dataset (dictionary of DataFrames) or a single DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame with merged stops information, including deduplication and joins
            across several GTFS files.
        """
        # Load partitions if necessary
        if not isinstance(gtfs_input, dict):
            gtfs_input = GTFSProcessor.load_partitions(gtfs_input)

        # Prepare output dictionary for combined data
        combined_data = {}

        # Define expected GTFS filenames
        gtfs_files = [
            'agency.txt', 'calendar.txt', 'calendar_dates.txt', 
            'routes.txt', 'stops.txt', 'stop_times.txt', 
            'trips.txt', 'frequencies.txt', 'transfers.txt', 'shapes.txt'
        ]

        # Process each partition
        for partition_name, df in gtfs_input.items():
            for filename in gtfs_files:
                # Check if the filename (without extension) is in the partition name (case-insensitive)
                if filename.replace('.txt', '') in partition_name.lower():
                    try:
                        if not df.empty:
                            if filename not in combined_data:
                                combined_data[filename] = df
                            else:
                                combined_data[filename] = pd.concat([combined_data[filename], df], ignore_index=True)
                    except Exception as e:
                        print(f"Error processing {partition_name}: {str(e)}")

        # Deduplicate combined data per file type
        for filename, df in combined_data.items():
            try:
                if 'trip_id' in df.columns:
                    key_columns = [col for col in df.columns if any(key in col for key in ['trip_id', 'route_id', 'service_id'])]
                    df = df.drop_duplicates(subset=key_columns, keep='last')
                elif 'stop_id' in df.columns:
                    df = df.drop_duplicates(subset=['stop_id'], keep='last')
                elif 'route_id' in df.columns:
                    df = df.drop_duplicates(subset=['route_id'], keep='last')
                elif filename == 'calendar.txt':
                    df = df.drop_duplicates(subset=['service_id', 'start_date', 'end_date'], keep='last')
                    df.dropna(subset=['start_date', 'end_date'], inplace=True)
                elif filename == 'calendar_dates.txt':
                    df = df.drop_duplicates(subset=['service_id', 'date'], keep='last')
                else:
                    df = df.drop_duplicates(keep='last')
                combined_data[filename] = df
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

        # Perform the final join to create stops_df
        stops_df = (
            combined_data['stop_times.txt'][['trip_id', 'arrival_time', 'stop_id', 'stop_sequence']]
            .merge(
                combined_data['stops.txt'][['stop_id', 'stop_code', 'stop_lat', 'stop_lon', 'stop_name']], 
                on='stop_id', 
                how='left'
            )
            .merge(
                combined_data['trips.txt'][['trip_id', 'route_id', 'service_id', 'direction_id', 'shape_id']], 
                on='trip_id', 
                how='left'
            )
            .merge(
                combined_data['calendar.txt'][['service_id', 'start_date', 'end_date']], 
                on='service_id', 
                how='left'
            )
            .merge(
                combined_data['shapes.txt'][['shape_id', 'shape_pt_sequence', 'shape_pt_lat', 'shape_pt_lon']],
                how='left',
                left_on=['shape_id', 'stop_lat', 'stop_lon'],
                right_on=['shape_id', 'shape_pt_lat', 'shape_pt_lon']
            )
        )

        # Convert date fields and extract year
        stops_df['start_date'] = pd.to_datetime(stops_df['start_date'], format='%Y%m%d')
        stops_df['end_date'] = pd.to_datetime(stops_df['end_date'], format='%Y%m%d')
        stops_df['year'] = stops_df['start_date'].dt.year

        return stops_df
