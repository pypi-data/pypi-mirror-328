import pandas as pd
from gs_ml_toolkit.direction_processor import DirectionProcessor
from mapping_for_test import mapping_linee

def test_direction_processor_basic():
    # Setup
    mapping = {}
    processor = DirectionProcessor(mapping)

    df = pd.DataFrame({
        'stop_code': [1,2],
        'route_id': [100,100],
        'year': [2021,2021],
        'Direzione': [None, None]
    })

    gtfs_df = pd.DataFrame({
        'route_id': ['100','100'],
        'stop_code': [1,2],
        'year': [2021,2021],
        'direction_id': [0,0],
        'stop_sequence': [10,20],
        'stop_name': ['Stop A', 'Stop B']
    })

    # Action
    result_df = processor.create_direction_sequence(
        df, gtfs_df, 'stop_code', 'route_id',
        'stop_sequence_salita', 'stop_name'
    )

    # Assert
    assert not result_df['Direzione'].isna().all(), "Direction should be assigned"


def test_direction_evasion():
    # Setup
    processor = DirectionProcessor(mapping_linee)

    # Carica i CSV di test
    df = pd.read_csv("data_for_testing/evasion_test.csv")
    gtfs_df = pd.read_csv("data_for_testing/gtfs_test.csv")

    # Action
    result_df = processor.create_direction_sequence(
        df, gtfs_df,
        stop_col_id="id_fermata_salita",
        route_col_id="linea",
        stop_sequence_col="stop_sequence_salita",
        stop_name_col="stop_name"
    )

    # Assert di base
    assert not result_df.empty, "Il DataFrame risultante non dovrebbe essere vuoto."
    assert not result_df['Direzione'].isna().all(), "Almeno una Direzione dovrebbe essere assegnata."
    assert 'stop_sequence_salita' in result_df.columns, "Manca la colonna stop_sequence_salita."
    assert 'stop_name' in result_df.columns, "Manca la colonna stop_name."

    # Assert aggiuntivi
    assert pd.api.types.is_numeric_dtype(result_df['Direzione']), "Direzione dovrebbe essere numerico."
    assert pd.api.types.is_numeric_dtype(result_df['stop_sequence_salita']), "stop_sequence_salita dovrebbe essere numerico."
    assert len(result_df) <= len(df), "La funzione non dovrebbe aumentare il numero di righe."


def test_direction_occupancy():
    # Setup
    processor = DirectionProcessor(mapping_linee)
                                                                                                                                            
    # Carica i CSV di test
    df = pd.read_csv("data_for_testing/occupancy_test.csv", low_memory=False)
    gtfs_df = pd.read_csv("data_for_testing/gtfs_test.csv")

    # Action
    result_df = processor.create_direction_sequence(
        df, gtfs_df,
        stop_col_id="ID Fermata",
        route_col_id="Linea",
        stop_sequence_col="Ordine Fermata",
        stop_name_col="Descrizione Fermata"
    )

    # Assert di base
    assert not result_df.empty, "Il DataFrame risultante non dovrebbe essere vuoto."
    assert not result_df['Direzione'].isna().all(), "Almeno una Direzione dovrebbe essere assegnata."
    assert 'Ordine Fermata' in result_df.columns, "Manca la colonna 'Ordine Fermata'."
    assert 'Descrizione Fermata' in result_df.columns, "Manca la colonna 'Descrizione Fermata'."

    # Assert aggiuntivi
    assert pd.api.types.is_numeric_dtype(result_df['Direzione']), "Direzione dovrebbe essere numerico."
    assert pd.api.types.is_numeric_dtype(result_df['Ordine Fermata']), "'Ordine Fermata' dovrebbe essere numerico."
    # In questo caso 'Descrizione Fermata' potrebbe essere stringhe
    assert len(result_df) <= len(df), "La funzione non dovrebbe aumentare il numero di righe."
