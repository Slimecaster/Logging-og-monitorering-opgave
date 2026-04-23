# myapp.py
import logging
import controller

def main():
    # Configure logging
    logging.basicConfig(
        filename='myapp.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    
    try:
        logger.info('Started')
        controller.do_something()
        controller.run()
    except KeyboardInterrupt:
        logger.info('Server stopped by user')
    except Exception as e:
        logger.critical(f'Server stopped unexpectedly: {e}')

if __name__ == '__main__':
    main()