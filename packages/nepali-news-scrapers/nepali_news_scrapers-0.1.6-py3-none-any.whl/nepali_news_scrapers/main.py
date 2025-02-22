import click
from services.scraper_service import ScraperRunner


@click.command()
@click.option("--name", help="Enter the name of the scraper to run")
def run_scraper(name):

    scraper_instance = ScraperRunner.get_scraper_instance(name)

    scraper_instance.start()


if __name__ == "__main__":
    run_scraper()
