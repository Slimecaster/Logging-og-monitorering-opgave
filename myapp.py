import logging

# 1. Create a logger
logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)  # capture everything; handlers decide what to show

# 2. Create a formatter (how log lines look)
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# 3. Console handler - prints to terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# 4. File handler - writes to app.log
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# 5. Attach the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# --- Example usage ---
def main():
    logger.info("Application started")

    logger.debug("This is a debug message (only goes to file)")
    logger.info("Everything is running normally")
    logger.warning("Something looks off, but we can continue")
    logger.error("Something failed")
    logger.critical("Something failed badly")
    logger.info("Application finished")


if __name__ == "__main__":
    main()