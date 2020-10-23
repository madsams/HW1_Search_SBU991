from apscheduler.schedulers.twisted import TwistedScheduler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
scheduler = TwistedScheduler()
process.crawl('dollar')  # run for the first time
scheduler.add_job(process.crawl, 'interval', args=['dollar'], seconds=24 * 60 * 60 * 60)
scheduler.start()
process.start(False)
