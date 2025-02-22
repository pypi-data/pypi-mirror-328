import logging
from collections.abc import Iterable

from ...utils import (
    OUTPUT_DIR,
    current_timestamp,
    deep_serialize,
    from_env,
    get_output_filename,
    write_errors_logs,
    write_json,
    write_summary,
)
from .assets import TableauAsset
from .client import ApiClient as Client

logger = logging.getLogger(__name__)


def iterate_all_data(
    client: Client,
) -> Iterable[tuple[TableauAsset, list]]:
    """Iterate over the extracted Data from Tableau"""

    logger.info("Extracting USER from Tableau API")
    yield TableauAsset.USER, deep_serialize(client.fetch(TableauAsset.USER))

    logger.info("Extracting WORKBOOK from Tableau API")
    yield (
        TableauAsset.WORKBOOK,
        deep_serialize(
            client.fetch(TableauAsset.WORKBOOK),
        ),
    )

    logger.info("Extracting DASHBOARD from Tableau API")
    yield (
        TableauAsset.DASHBOARD,
        deep_serialize(
            client.fetch(TableauAsset.DASHBOARD),
        ),
    )

    logger.info("Extracting PUBLISHED DATASOURCE from Tableau API")
    yield (
        TableauAsset.PUBLISHED_DATASOURCE,
        deep_serialize(
            client.fetch(TableauAsset.PUBLISHED_DATASOURCE),
        ),
    )

    logger.info("Extracting PROJECT from Tableau API")
    yield (
        TableauAsset.PROJECT,
        deep_serialize(
            client.fetch(TableauAsset.PROJECT),
        ),
    )

    logger.info("Extracting USAGE from Tableau API")
    yield TableauAsset.USAGE, deep_serialize(client.fetch(TableauAsset.USAGE))

    logger.info("Extracting WORKBOOK_TO_DATASOURCE from Tableau API")
    yield (
        TableauAsset.WORKBOOK_TO_DATASOURCE,
        deep_serialize(
            client.fetch(TableauAsset.WORKBOOK_TO_DATASOURCE),
        ),
    )

    logger.info("Extracting DATASOURCE from Tableau API")
    yield (
        TableauAsset.DATASOURCE,
        deep_serialize(
            client.fetch(TableauAsset.DATASOURCE),
        ),
    )

    logger.info("Extracting CUSTOM_SQL_TABLE from Tableau API")
    yield (
        TableauAsset.CUSTOM_SQL_TABLE,
        deep_serialize(
            client.fetch(TableauAsset.CUSTOM_SQL_TABLE),
        ),
    )

    logger.info("Extracting CUSTOM_SQL_QUERY from Tableau API")
    yield (
        TableauAsset.CUSTOM_SQL_QUERY,
        deep_serialize(
            client.fetch(TableauAsset.CUSTOM_SQL_QUERY),
        ),
    )

    logger.info("Extracting FIELD from Tableau API")
    yield TableauAsset.FIELD, deep_serialize(client.fetch(TableauAsset.FIELD))


def extract_all(client: Client, **kwargs: str) -> None:
    """
    Extract Data from tableau
    Store data locally in files under the output_directory
    If errors from Tableau's API are catch store them locally in file under the output_directory
    """
    output_directory = kwargs.get("output_directory") or from_env(OUTPUT_DIR)

    timestamp = current_timestamp()

    for key, data in iterate_all_data(client):
        filename = get_output_filename(key.value, output_directory, timestamp)
        write_json(filename, data)

    write_summary(
        output_directory,
        timestamp,
        base_url=client.base_url(),
        client_name=client.name(),
    )

    if client.errors:
        write_errors_logs(output_directory, timestamp, client.errors)
