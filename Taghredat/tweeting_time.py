import schedule
import time


class Tweeting_time:
    Stop_loop = False

    def tweet_function():
        print("last_image")

    def schedule_tweets(interval_minutes, total_tweets, function = tweet_function ,mode = "on"):
        Tweeting_time.Stop_loop = False
        if mode == "on":
                x = 1
                schedule.every(interval_minutes).seconds.do(function)  # Passing the function, not calling it
                while x <= total_tweets and not Tweeting_time.Stop_loop :
                        schedule.run_pending()
                        if x  < total_tweets :
                            time.sleep(interval_minutes)    
                            x += 1
                        else:
                            break           
        elif mode == "off" :
            schedule.clear()
            schedule.cancel_job(function)
    
    def cancel():
        try:
            schedule.clear()
            schedule.cancel_job()
        except:
            Tweeting_time.Stop_loop = True