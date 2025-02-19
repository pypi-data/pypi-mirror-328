import click
import json
import sys
from nomad_media_cli.helpers.utils import initialize_sdk

@click.command()
@click.option("--schedule-id", required=True, help="The ID of the schedule the schedule item asset is to be updated from.")
@click.option("--item-id", required=True, help="The ID of the item to be updated.")
@click.option("--asset", required=False, help="The asset of the schedule item asset in JSON dict format.")
@click.option("--days", required=False, help="The days of the schedule item asset in JSON list format.")
@click.option("--duration-time-code", required=False, help="The duration time between time_code and end_time_code. Format: hh:mm:ss;ff.")
@click.option("--end-time-code", required=False, help="The end time code of the schedule item asset. Format: hh:mm:ss;ff.")
@click.option("--time-code", required=False, help="The time code of the schedule item asset. Format: hh:mm:ss;ff.")
@click.pass_context
def update_schedule_item_asset(ctx, schedule_id, item_id, asset, days, duration_time_code, end_time_code, time_code):
    """Update schedule item asset"""
    initialize_sdk(ctx)
    nomad_sdk = ctx.obj["nomad_sdk"]

    try:
        result = nomad_sdk.update_schedule_item_asset(
            schedule_id,
            item_id,
            json.loads(asset) if asset else None,
            json.loads(days) if days else None,
            duration_time_code,
            end_time_code,
            time_code
        )
        click.echo("Schedule item asset updated successfully.")
        click.echo(json.dumps(result, indent=4))

    except Exception as e:
        click.echo(json.dumps({"error": f"Error updating schedule item asset: {e}"}))
        sys.exit(1)