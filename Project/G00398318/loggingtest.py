import logging

logging.basicConfig(format = '%(asctime)s %(message)s',
                    datefmt = '%m/%d/%Y %I:%M:%S %p',
                    filename = 'example.log',
                    level=logging.DEBUG) 
logging.info('Forecasting Job Started...')
logging.debug('abc method started...')