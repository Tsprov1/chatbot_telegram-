from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests 
import os
import datetime 
from telegram import InputFile
import random 
import openai
import wikipedia
import qrcode
from io import BytesIO

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

    image_paths = [
        r"d:\SDcard\DCIM\Camera\IMG_20210307_102324.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210331_115221.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210407_083947.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210407_084019.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210417_080457.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210417_080505.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210417_080515.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210417_105925.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210417_105929.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210421_100448.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210421_100526.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210421_100531.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210802_175353.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210804_175643.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210804_180117.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210809_082338.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210809_083941.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210809_130451.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210809_132418.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210809_132425.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210809_132428.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210810_091743.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210810_092743.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210811_125317.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210811_154033.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210811_154048.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210811_163803.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210813_073553.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210817_171745.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210817_171759.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210819_100824.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210819_105748.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210823_184908.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210825_070449.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_075846 1.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_075846.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_174938.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_180152.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_180218.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_180627.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_180819.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_181404.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210826_181606.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210828_211444.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210829_213614.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210930_154026.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20210930_154033.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211002_184853.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211006_144203.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211009_203950.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211011_093524.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211018_170243.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211022_163024.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211022_175559.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211023_112829.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211028_222801.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20211028_222830.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220321_083529.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220324_101312.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220324_101320.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220324_101915.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220324_101917.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220402_213628.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220408_201752.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220411_065340.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220414_171010.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220415_141705.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220416_130917.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220503_152809.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220508_220257.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220508_220633.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220510_095019.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220510_095098.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220510_095512.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220517_200731.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220703_164529.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220713_171556.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220808_170028.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220814_165542.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220814_165609_Burst01.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220925_154504.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220925_154559.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220925_172830.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220926_192102.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20220928_132309.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20221023_060943.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20221101_204558.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230604_220752.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230604_220757.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230604_220759.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230604_220804.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230613_061021.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230619_152759.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230619_152800.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230619_175846.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230619_175856.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230619_175924.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230623_202704.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230623_202707.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230629_113032.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230629_170516.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230629_170519.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230629_201425.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230630_212438.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230702_142221.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230715_100820.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230717_184101.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230718_175508.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230718_175517.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230718_175543.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230718_175549.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230724_173711.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230724_173716.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230724_173726.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230802_182948.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230802_182953.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230802_183006.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230802_183014.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230822_095349.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230822_095503.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230822_095504.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230827_193746.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230827_193754.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230827_193758.jpg",
        r"d:\SDcard\DCIM\Camera\IMG_20230827_193835.jpg"
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
    await update.message.reply_text('Bot này hỗ trợ các lệnh sau:')
    commands = [
        "/hello - Chào hỏi",
        "/help - Hướng dẫn sử dụng bot",
        "/weather <thành phố> - Xem thời tiết (ví dụ: /weather Hanoi)",
        "/photo - Gửi ảnh mẫu và ảnh từ thư mục",
        "/video - Gửi video mẫu và video từ thư mục",
        "/link - Liên kết Facebook, Github, Zalo",
        "/news - Tin tức mới nhất về Việt Nam",
        "/send_files <thư mục> - Gửi file từ thư mục (ví dụ: /send_files D:/tailieu)",
        "/ask <câu hỏi> - Hỏi AI ChatGPT (ví dụ: /ask TSPRO là ai?)",
        "/wiki <từ khóa> - Tóm tắt Wikipedia (ví dụ: /wiki định luật II newton)",
        "/qr <nội dung> - Tạo mã QR (ví dụ: /qr TSPRO)",
    ]
    for cmd in commands:
        await update.message.reply_text(cmd)
    await update.message.reply_text('Bạn hãy nhập lệnh để trải nghiệm!')

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

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("Bạn hãy nhập câu hỏi sau /ask.")
        return
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    answer = response.choices[0].message.content
    await update.message.reply_text(answer)

async def wiki(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Bạn hãy nhập từ khóa sau /wiki.")
        return
    try:
        summary = wikipedia.summary(query, sentences=3)
        await update.message.reply_text(summary)
    except Exception as e:
        await update.message.reply_text(f"Không tìm thấy thông tin: {e}")

async def qr(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Bạn hãy nhập nội dung sau /qr.")
        return
    img = qrcode.make(text)
    bio = BytesIO()
    img.save(bio, format='PNG')
    bio.seek(0)
    await update.message.reply_photo(photo=InputFile(bio, filename="qr.png"))


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
app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("wiki", wiki))
app.add_handler(CommandHandler("qr", qr))

app.run_polling()
