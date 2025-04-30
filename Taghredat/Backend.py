from flet import * 
from Images import Choose_image
from folder_path import Folder_path
from tweeting_time import Tweeting_time
from GPT_X import GPT_x
from history import History
import tweepy

class backend:
    tweet_counter = 0
    number_of_untweets = 0
    hours = 0
    minutes = 0
    seconds = 0

    def update_display(page:Page,text:Text):
        text.value = f"{backend.hours:02}:{backend.minutes:02}:{backend.seconds:02}"
        page.update()

    def increment_hours(e,page:Page,text:Text):
        backend.hours = (backend.hours + 1) % 24
        backend.update_display(page,text)

    def decrement_hours(e,page:Page,text:Text):
        backend.hours = (backend.hours - 1) % 24
        backend.update_display(page,text)
        

    def increment_minutes(e,page:Page,text:Text):
        backend.minutes = (backend.minutes + 1) % 60
        backend.update_display(page,text)


    def decrement_minutes(e,page:Page,text:Text):
        backend.minutes = (backend.minutes - 1) % 60
        backend.update_display(page,text)


    def increment_seconds(e,page:Page,text:Text):
        backend.seconds = (backend.seconds + 1) % 60
        backend.update_display(page,text)


    def decrement_seconds(e,page:Page,text:Text):
        backend.seconds = (backend.seconds - 1) % 60
        backend.update_display(page,text)

    
    @staticmethod
    def on_change_textfeild(page:Page,text_feild:TextField,button:IconButton):
        if text_feild.value == "":
            button.disabled = True
        else:
            button.disabled = False
        page.update()

    #! وبيحفظ مسار المجلد الي المستخدم اختاره
    @staticmethod
    def file_pick_result (e:FilePickerResultEvent,page:Page):
        try:
            Folder_path.save_folder_path(e.path)
            page.update()
        except TypeError:
            pass
    
    @staticmethod
    def last_image_repeat(last_image:str,folder_path:str):
        if last_image != None:
            pass
        else:
            Choose_image.re_use_images()
            last_image = Choose_image.the_last_image(folder_path)
        return last_image
    
    def response_len(link:Checkbox,response:str):
        if link.value == True:
            response = response + "\nhttps://ajeers.com/visit"
        else:
            pass
        return response

    #?======================= دي علشان توليد البوستات و الصور من الجهاز ========================
    @staticmethod
    def post_mange(page:Page,image:Image,counter:Text,number_of_posts:TextField,output_topic:TextField,input_topic:TextField,
                   snackbar:SnackBar,snackbar_text:Text,number_of_letters:Text,link:Checkbox):
        try:

            
            backend.tweet_counter += 1
            output_topic.visible = image.visible = True
            folder_path = Folder_path.read_folder_path()
            last_image = Choose_image.the_last_image(folder_path)

            if str(last_image).endswith(".mp4"):
                image.visible = False
                pass
            else:
                last_image = str(backend.last_image_repeat(last_image,folder_path))
                image.src = str(backend.last_image_repeat(last_image,folder_path))

            prompt = input_topic.value
            response = GPT_x.generate_response(prompt) 
            response = backend.response_len(link,response)
            
            counter.value = f"{backend.tweet_counter}/{number_of_posts.value} = عدد التغريدات "
            output_topic.value = response

            if len(response) > 280:
                try:
                    raise tweepy.Forbidden(response=f'{response}')
                except AttributeError:
                    backend.number_of_untweets += 1
                    number_of_letters.value = f"{backend.number_of_untweets} = عدد التغريدات الغير منشورة  "
                    snackbar.open = True
                    snackbar_text.value = "تم تجاوز الحد الأقصى للعدد الحروف المستخدمة في التغريدة" 
                    pass
            else:
                # GPT_x.Upload_in_Twitter(f'{response}',media_path=last_image)
                pass
           
        except FileNotFoundError:
            output_topic.visible = image.visible = False
            snackbar.open = True
            snackbar_text.value = "يجب إرفاق مسار الملف الخاص بالصور ,الرجاء التاكد من ارفاق المسار واعادة المحاولة"
        except TypeError:
            output_topic.visible = image.visible = False
            snackbar.open = True
            snackbar_text.value = "يجب إرفاق مسار الملف الخاص بالصور ,الرجاء التاكد من ارفاق المسار واعادة المحاولة"
        except tweepy.Forbidden:
            snackbar.open = True
            snackbar_text.value = "تم تجاوز الحد الأقصى للعدد الحروف المستخدمة في التغريدة"

        except SyntaxError:
            pass

        page.update()

    #! دي المفروض بتاعت توليد التويتات 
    @staticmethod
    def generete_tweet(page:Page,number_of_posts:TextField,image:Image,
                       snackbar:SnackBar,snackbar_text:Text,time_gap:Text,counter:Text,output_topic:TextField,input_topic:TextField,number_of_letters:Text,link:Checkbox):
        try:  
            snackbar.open = True
            snackbar_text.value = "سيتم رفع التغريدات المطلوبة"
            backend.tweet_counter = backend.number_of_untweets = 0 
            number_of_letters.value = f"{backend.number_of_untweets} = عدد التغريدات الغير منشورة  "
            seconds = backend.hours * 3600 + backend.minutes * 60 + backend.seconds
            time_gap.value = f"{backend.hours:02}:{backend.minutes:02}:{backend.seconds:02} = الوقت المستغرق ما بين كل تغريدة وتغريدة"    
            History.Add_to_history(input_topic.value)   
            Tweeting_time.schedule_tweets(interval_minutes=seconds,total_tweets=int(number_of_posts.value)+1,function=lambda:backend.post_mange(page,image,counter ,number_of_posts,output_topic,input_topic,snackbar,snackbar_text,number_of_letters,link))
            snackbar.open = True
            snackbar_text.value = "تم الإنتهاء من رفع التغريدات المطلوبة"
            Tweeting_time.cancel()
        except ValueError: 
            snackbar_text.value = "يجب ادخال رقم محدد في خانة ( عدد التغريدات عن هذا الموضوع )"
            snackbar.open = True    
        page.update()  
            

    #! دي علشان الغي عمليات توليد التغريدات 
    @staticmethod
    def Cancel_generating_tweets(page:Page,image:Image,counter:Text,number_of_posts:TextField,output_topic:TextField,input_topic:TextField,
                   snackbar:SnackBar,snackbar_text:Text,number_of_letters:Text,link:Checkbox):
        
        Tweeting_time.cancel()
        snackbar_text.value = "تم الغاء عمليات التغريد السابقة"
        snackbar.open = True
        page.update()
    
    #! دي علشان اخلي المستخدم يعرف يستخدم الصور تاني 
    @staticmethod
    def re_use_image(page:Page,snackbar:SnackBar,snackbar_text:Text):
        Choose_image.re_use_images()
        snackbar_text.value = "يمكنك الآن استخدام الصور مرة اخرى "
        snackbar.open = True
        page.update()

    @staticmethod
        
    def Clear_interface(page:Page,image:Image,output_topic:TextField,input_topic:TextField,counter:Text,time_gap:Text,number_of_letters:Text):
        image.visible = False
        output_topic.visible = False
        output_topic.value = ""
        input_topic.value = ""
        counter.value = ""
        time_gap.value= ""
        number_of_letters.value = ""
        page.update()