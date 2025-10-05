from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests 
import os
import datetime 
from telegram import InputFile
import random 

#       HELLO
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'welcome to TSPRO :3 ) ')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#    WEATHER
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7)))
    await update.message.reply_text(f"Bây giờ là {now.strftime('%H:%M:%S')} tại Việt Nam.")

    if context.args:
        city = " ".join(context.args)
    else:
        city = "Hà Nội"
    api_key = "4194bc8a9f0a6201907bb33ef2dfb5c2"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=vi"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        await update.message.reply_text(f"Thời tiết tại {city}: {desc}, nhiệt độ: {temp}°C")
    else:
        await update.message.reply_text("Không tìm thấy thông tin thời tiết cho thành phố này.")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------



#    PICTURE
#-----------------------------------------------------------------------------------------------------------------------------------------------------------    
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_photo("https://photos.app.goo.gl/4uF3DKZbW6mwV9L26")

    image_paths = [
        r"D:\SDcard\DCIM\Camera\IMG_20241126_203735.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241128_074118.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241128_074454.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241128_074854.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241128_075201.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241128_080047.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241128_080333.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241128_080335.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241126_174354.jpg",
r"D:\SDcard\DCIM\Camera\IMG_20241126_174617.jpg"
    ]
    for path in image_paths:
        with open(path, "rb") as photo_file:
            await update.message.reply_photo(photo=InputFile(photo_file))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#         VIDEO
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
async def video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_video("https://drive.google.com/uc?export=download&id=1I36b9RaXDIGiihdG0OWAb9YkH3_R5xaB")

    video_paths = [
        r"F:\video\12t91gh5.jpeg",
        r"F:\video\16rtufp.mp4",
        r"F:\video\ms8xv6.mp4",
        r"F:\video\ms8xv9.mp4",
        r"F:\video\16rtufq.mp4",
        r"F:\video\16rtufr.mp4"
    ]
    for path in video_paths:
        with open(path, "rb") as video_file:
            await update.message.reply_video(video=InputFile(video_file))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#        SEND LINK
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text("FB : https://www.facebook.com/tspromax")
    await update.message.reply_text("Github : https://github.com/Tsprov1")
    await update.message.reply_text("Zalo : https://zalo.me/0862067001")






#             HELP
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f' Tôi có thể giúp gì cho bạn?')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------



#          LIST
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Chào mừng bạn đến với bot của chúng tôi!')
    commands = [
        "/hello - Chào hỏi",
        "/help - Hướng dẫn",
        "/weather - Xem thời tiết",
        "/photo - Gửi ảnh",
        "/video - Gửi video",
        "/link - Liên kết"
        ,"/news - Tin tức mới "
        ,"/send_files - Gửi file "
    ]
    await update.message.reply_text("Các lệnh bạn có thể dùng:")
    for cmd in commands:
        await update.message.reply_text(cmd)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#          NEWS 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    api_key = "2a8a4745051c4f9386dafcdac47c4a24"  # Thay bằng API key của bạn
    url = f"https://newsapi.org/v2/everything?q=việt nam&sortBy=publishedAt&pageSize=5&language=vi&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        if articles:
            for article in articles:
                title = article.get("title", "Không có tiêu đề")
                link = article.get("url", "")
                image_url = article.get("urlToImage", None)
                message = f"{title}\n{link}"
                if image_url:
                    await update.message.reply_photo(photo=image_url, caption=message)
                else:
                    await update.message.reply_text(message)
        else:
            await update.message.reply_text("Không tìm thấy tin tức mới.")
    else:
        await update.message.reply_text("Không thể lấy tin tức vào lúc này.")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#         SEND_FILE
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
async def send_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   
    folder_paths = context.args if context.args else [
        
        r"D:\tailieuhoctapxyz\toán 2\Toán VL 2"
        
    ]

    for folder_path in folder_paths:
        if not os.path.exists(folder_path):
            await update.message.reply_text(f"Thư mục không tồn tại: {folder_path}")
            continue

        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if not files:
            await update.message.reply_text(f"Không có file nào trong thư mục: {folder_path}")
            continue

        await update.message.reply_text(f"Gửi file từ thư mục: {folder_path}")
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "rb") as f:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    await update.message.reply_photo(photo=InputFile(f), caption=filename)
                elif filename.lower().endswith(('.mp4', '.mov', '.avi')):
                    await update.message.reply_video(video=InputFile(f), caption=filename)
                else:
                    await update.message.reply_document(document=InputFile(f), caption=filename)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------



app = ApplicationBuilder().token("8306680899:AAFeG5NXM0N_fPDbFiF2GWbF-2M5yVFiS9U").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("weather", weather))
app.add_handler(CommandHandler("photo", photo))
app.add_handler(CommandHandler("video", video))
app.add_handler(CommandHandler("link", link))
app.add_handler(CommandHandler("news", news ))
app.add_handler(CommandHandler("send_files", send_files))

app.run_polling()
