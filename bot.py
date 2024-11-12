import logging
import os
import zipfile
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import instaloader
import config

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Instaloader
L = instaloader.Instaloader()

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Instagram Download Bot! Use /download <username> to download a profile.')

# Download command handler
def download(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 1:
        update.message.reply_text('Usage: /download <username>')
        return

    username = context.args[0]
    try:
        # Log in if necessary (for private profiles)
        # Uncomment the following line and provide your credentials if needed
        # L.login(config.INSTAGRAM_USERNAME, config.INSTAGRAM_PASSWORD)

        # Download the profile
        update.message.reply_text(f'Starting download for {username}...')
        L.download_profile(username, profile_pic_only=False)

        # Check if zip feature is enabled
        if config.ZIP_ENABLED:
            zip_directory(username)

        update.message.reply_text(f'Download completed for {username}.')
    except instaloader.exceptions.ProfileNotExistsException:
        update.message.reply_text(f'Profile {username} does not exist.')
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        update.message.reply_text(f'Profile {username} is private and not followed.')
    except Exception as e:
        logger.error(f'Error downloading {username}: {e}')
        update.message.reply_text('An error occurred while downloading the profile.')

# Function to zip downloaded files
def zip_directory(username: str) -> None:
    folder_path = os.path.join(os.getcwd(), username)
    zip_file_path = f'{username}.zip'
    
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)

    logger.info(f'Zipped files for {username} into {zip_file_path}')

# Main function to start the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(config.TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
