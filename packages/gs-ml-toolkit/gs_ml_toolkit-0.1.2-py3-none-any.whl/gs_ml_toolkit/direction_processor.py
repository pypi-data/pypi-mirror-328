import re
import numpy as np
import pandas as pd
from functools import partial


class DirectionProcessor:
    def __init__(self, mapping_linee: dict, confidence_score: float = 0.7):
        """
        Initializes the processor.

        :param mapping_linee: A dictionary mapping GTFS route IDs.
        :param confidence_score: Confidence threshold to consider a direction valid.
        """
        self.mapping_linee = mapping_linee
        self.confidence_score = confidence_score

    @staticmethod
    def is_snake_case(columns) -> bool:
        """
        Check if all provided column names are in snake_case.
        """
        return all(re.match(r'^[a-z0-9_]+$', col) for col in columns)

    @staticmethod
    def calculate_direction_distribution(df: pd.DataFrame, group_cols: list, confidence_score: float) -> dict:
        """
        Calculate the direction distribution and returns a mapping of keys (group values)
        to the most common direction if its confidence is above the threshold.

        :param df: Input DataFrame.
        :param group_cols: List of columns to group by.
        :param confidence_score: Confidence threshold.
        :return: Dictionary mapping group tuples to direction_id.
        """
        direction_distribution = (
            df.groupby(group_cols)['direction_id']
              .agg(lambda x: x.value_counts(normalize=True).to_dict())
              .reset_index()
        )

        direction_map = {}
        for _, row in direction_distribution.iterrows():
            key = tuple(row[col] for col in group_cols)
            directions = row['direction_id']
            # Find the direction with the highest confidence
            max_direction = max(directions, key=directions.get)
            max_confidence = directions[max_direction]
            if max_confidence >= confidence_score:
                direction_map[key] = max_direction

        return direction_map

    @staticmethod
    def get_direction_year(row: pd.Series, direction_map_with_year: dict, stop_col_id: str, route_col_id: str):
        """
        Returns the direction based on stop, route, and year using the provided mapping.
        """
        combo = (row[stop_col_id], row[route_col_id], row['year'])
        return direction_map_with_year.get(combo, np.nan)

    @staticmethod
    def get_direction(row: pd.Series, direction_map_without_year: dict, stop_col_id: str, route_col_id: str):
        """
        Returns the direction based on stop and route using the provided mapping.
        """
        combo = (row[stop_col_id], row[route_col_id])
        return direction_map_without_year.get(combo, np.nan)

    @staticmethod
    def fill_direction_by_trip_mode(group: pd.DataFrame) -> pd.Series:
        """
        For a group (trip), fill missing directions with the mode (most common direction).
        If no valid direction exists, returns the group unchanged.
        Assumes the grouping column ('trip_id') has been dropped.
        """
        if group['Direzione'].isna().all():
            return group['Direzione']

        mode_direction = group['Direzione'].mode().iloc[0]
        return group['Direzione'].fillna(mode_direction)

    @staticmethod
    def uniformize_directions(group: pd.DataFrame) -> pd.DataFrame:
        """
        For a group, if more than one direction is present and one of them is the majority (>=50%),
        set all directions in the group to that majority direction.
        Assumes the grouping column ('trip_id') has been dropped.
        """
        group = group.copy()
        if len(group) <= 1:
            return group
        direction_counts = group['Direzione'].value_counts()
        if len(direction_counts) > 1:
            majority_direction = direction_counts.idxmax()
            if direction_counts[majority_direction] / len(group) >= 0.5:
                group['Direzione'] = majority_direction
        return group

    def create_direction_sequence(
        self,
        df: pd.DataFrame,
        gtfs_df: pd.DataFrame,
        stop_col_id: str,
        route_col_id: str,
        stop_sequence_col: str,
        stop_name_col: str
    ) -> pd.DataFrame:
        """
        Process the input DataFrame 'df' and the GTFS DataFrame 'gtfs_df' to calculate
        the direction sequences, filling missing values based on GTFS mapping and trip modes.

        :param df: The DataFrame to update with direction and stop information.
        :param gtfs_df: GTFS DataFrame containing route, stop, and direction data.
        :param stop_col_id: Column name in df representing the stop code.
        :param route_col_id: Column name in df representing the route id.
        :param stop_sequence_col: Column name to be created for stop sequence.
        :param stop_name_col: Column name to be created for stop name.
        :return: Modified df with added/updated direction and stop columns.
        """
        # Normalize GTFS column names if needed
        if not self.is_snake_case(gtfs_df.columns):
            gtfs_df.columns = (
                gtfs_df.columns.str.lower()
                .str.replace(" ", "_")
                .str.replace("'", "")
                .str.replace(" ", "-")
            )
        
        # Clean and map route_id
        gtfs_df['route_id'] = gtfs_df['route_id'].str.replace("-", "")
        gtfs_df['route_id'] = gtfs_df['route_id'].map(self.mapping_linee).fillna(gtfs_df['route_id'])
        gtfs_df['route_id'] = pd.to_numeric(gtfs_df['route_id'], errors='coerce').astype('Int64')
        gtfs_df.dropna(subset=['route_id'], inplace=True)

        # Ensure stop column is int type in df
        df[stop_col_id] = df[stop_col_id].astype(int)

        if 'trip_id' in df.columns: #If the data is occupancy data, add direction based on stop_code and stop_sequence

            group_cols_with_year = ['stop_code', 'stop_sequence', 'year']
            direction_map_with_year = self.calculate_direction_distribution(
                gtfs_df, group_cols_with_year, self.confidence_score
            )

            df['Direzione'] = df.apply(
            lambda row: self.get_direction_year(row, direction_map_with_year, stop_col_id, stop_sequence_col),
            axis=1
            )
            df.sort_index(inplace=True)
            df['Direzione'] = pd.to_numeric(df['Direzione'], errors='coerce')

            # Second pass: without year
            group_cols_without_year = ['stop_code', 'stop_sequence']
            direction_map_without_year = self.calculate_direction_distribution(
                gtfs_df, group_cols_without_year, self.confidence_score
            )

            mask_missing = df['Direzione'].isna()
            df.loc[mask_missing, 'Direzione'] = df[mask_missing].apply(
                lambda row: self.get_direction(row, direction_map_without_year, stop_col_id, stop_sequence_col),
                axis=1
            )
        else: #else add direction based on stop code and route_id, the data should be from evasion

            group_cols_with_year = ['stop_code', 'route_id', 'year']
            direction_map_with_year = self.calculate_direction_distribution(
                gtfs_df, group_cols_with_year, self.confidence_score
            )

            df['Direzione'] = df.apply(
                lambda row: self.get_direction_year(row, direction_map_with_year, stop_col_id, route_col_id),
                axis=1
            )

            df.sort_index(inplace=True)
            df['Direzione'] = pd.to_numeric(df['Direzione'], errors='coerce')

            # Second pass: without year
            group_cols_without_year = ['stop_code', 'route_id']
            direction_map_without_year = self.calculate_direction_distribution(
                gtfs_df, group_cols_without_year, self.confidence_score
            )

            mask_missing = df['Direzione'].isna()
            df.loc[mask_missing, 'Direzione'] = df[mask_missing].apply(
                lambda row: self.get_direction(row, direction_map_without_year, stop_col_id, route_col_id),
                axis=1
            )
            
        df.sort_index(inplace=True)
        df['Direzione'] = pd.to_numeric(df['Direzione'], errors='coerce')

        # If trip_id exists, fill missing directions based on trip mode and uniformize them
        if 'trip_id' in df.columns:
            # Process fill_direction_by_trip_mode without the grouping column to avoid warnings
            df['Direzione'] = (
                df
                .groupby('trip_id')
                .apply(lambda x: self.fill_direction_by_trip_mode(x))
                .reset_index(level=0, drop=True)
            )

            print(df.shape)
            
            # Process uniformize_directions without the grouping column to avoid warnings
            df = df.groupby('trip_id').apply(self.uniformize_directions).reset_index(drop=True)

        else:
            # Build mapping for stop_sequence and stop_name from GTFS
            mapping_stop_info_df = (
                gtfs_df
                .groupby(['route_id', 'direction_id', 'stop_code'])
                .agg(
                    stop_sequence=('stop_sequence', lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan),
                    stop_name=('stop_name', lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
                )
                .reset_index()
            )
            mapping_stop_info = {
                (row['route_id'], row['direction_id'], row['stop_code']):
                    (row['stop_sequence'], row['stop_name'])
                for _, row in mapping_stop_info_df.iterrows()
            }
            df[[stop_sequence_col, stop_name_col]] = df.apply(
                lambda row: pd.Series(
                    mapping_stop_info.get(
                        (row[route_col_id], row['Direzione'], row[stop_col_id]),
                        (np.nan, np.nan)
                    )
                ),
                axis=1
            )
        print(df.shape)
        df.dropna(subset=['Direzione'], inplace=True)

        return df
