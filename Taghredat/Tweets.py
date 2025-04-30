from flet import * 
from mode import Mode 
from Backend import *


class Window_1(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.page.window.icon = __file__.removesuffix("Tweets.py")+"twitter.ico"  
        self.page.scroll = ScrollMode.HIDDEN
        self.page.title = "تغريدات"
        self.page.window.resizable = page.window.maximizable = False
        self.page.window.center()
        #! ======================================================== Image ==================================================
        self.image_post = Image(src = "" , visible=False,height=200,width=200)
        self.Video = Video(visible=False,playlist_mode=PlaylistMode.LOOP,muted=True)
        #! ======================================================== Send Button ==================================================
        self.number_of_posts = TextField(label="عدد التغريدات عن هذا الموضوع",label_style=TextStyle(font_family="Andalus",size=20),rtl=True,width=300,focused_border_color=colors.BLUE_800,border_color="#36618e")
        self.number_of_posts_row = Row([self.number_of_posts],alignment=MainAxisAlignment.CENTER)
        self.row_increment = Row([IconButton(icons.ADD,on_click=lambda e:backend.increment_hours(e,self.page,self.timer)),IconButton(icons.ADD,on_click=lambda e:backend.increment_minutes(e,self.page,self.timer)),IconButton(icons.ADD,on_click=lambda e:backend.increment_seconds(e,self.page,self.timer))],alignment=MainAxisAlignment.CENTER)
        self.timer = Text(value=f"00:00:00",size=40)
        self.time_text_row = Row([self.timer],alignment=MainAxisAlignment.CENTER)
        self.row_decrement =  Row([IconButton(icons.REMOVE,on_click=lambda e:backend.decrement_hours(e,self.page,self.timer)),IconButton(icons.REMOVE,on_click=lambda e:backend.decrement_minutes(e,self.page,self.timer)),IconButton(icons.REMOVE,on_click=lambda e:backend.decrement_seconds(e,self.page,self.timer))],alignment=MainAxisAlignment.CENTER)
        self.null = Row([Text("")])
        

        self.open_sheet_send = Column([self.number_of_posts_row,self.null,self.row_increment,self.time_text_row,self.row_decrement],alignment=MainAxisAlignment.CENTER)
        self.send_button = IconButton(icons.SEND_ROUNDED,on_click=lambda _:  page.open(BottomSheet(self.open_sheet_send,on_dismiss=lambda _: backend.generete_tweet(self.page,self.number_of_posts,self.image_post,self.snackbar,self.snackbar_Text,self.time_gap,
                                                                                                                                                                                                                                            self.tweets_counter,self.output_topic,self.input_topic,self.number_of_letters,self.link_or_notlink))))
        
        #! ======================================================== Row0 (number of tweets ) =====================================================
        self.tweets_counter = Text(value="",font_family="Arial",size=20)
        self.time_gap = Text(value="",font_family="Arial",size=20)
        self.number_of_letters = Text(value="",font_family="Arial",size=20,color=colors.RED_700)
        #! ======================================================== Row1 (Input topic and image) ===================================================
        pick_files_dialog = FilePicker()
        self.upload =IconButton(icon=icons.ATTACH_FILE,on_click=lambda _: pick_files_dialog.get_directory_path())
        self.input_topic = TextField(label="الموضوع",rtl=True,label_style=TextStyle(font_family="Andalus",size=20),multiline=True,width=900,border_color="#36618e",border_width=2,on_change=lambda e: backend.on_change_textfeild(self.page,self.input_topic,self.send_button),on_focus=lambda e: backend.on_change_textfeild(self.page,self.input_topic,self.send_button))
        self.input_topic.focused_border_color = colors.BLUE_800
        self.input_topic.prefix = self.upload
        self.input_topic.suffix = self.send_button
        pick_files_dialog.on_result = lambda e: backend.file_pick_result(e=e,page=page)

        #! =========================================================== Row3 (RadioButton) =============================================================
        fill_color={
        ControlState.SELECTED: colors.LIGHT_BLUE_900,
        ControlState.HOVERED: colors.LIGHT_BLUE_800,
        ControlState.DEFAULT: "#dce3ef",
        }
        self.link_or_notlink= Checkbox(label="إضافة رابط مع التغريدة",fill_color=fill_color,label_style=TextStyle(size=12,color=colors.BLUE_800,weight=FontWeight.W_700),value=False,border_side=BorderSide(1,"White"),label_position=LabelPosition.LEFT) 
        

        #! =========================================================== Row3 (Buttons) =============================================================
        self.snackbar_Text = Text(value="",rtl=True)
        self.snackbar = SnackBar(content=self.snackbar_Text , open=False,show_close_icon=True)
        self.cancel_tweeting = ElevatedButton(tooltip="الغاء التغريدات الحالية",on_click= lambda e: backend.Cancel_generating_tweets(self.page,self.image_post,self.tweets_counter,self.number_of_posts,self.output_topic,self.input_topic,self.snackbar,self.snackbar_Text,self.number_of_letters,self.link_or_notlink),content=Row([Text("الغاء عمليات التغريد الحالية"),Icon(icons.CANCEL_ROUNDED)]))      
        # self.re_use_images = ElevatedButton(icon=icons.IMAGE_ROUNDED,text="إعادة استخدام الصور",on_click=lambda e: backend.re_use_image(self.page,self.snackbar,self.snackbar_Text))
        self.re_use_images = ElevatedButton(tooltip="مسح محتويات الشاشة",on_click=lambda e: backend.Clear_interface(self.page,self.image_post,self.output_topic,self.input_topic,self.tweets_counter,self.time_gap,self.number_of_letters),content=Row([Text("مسح"),Icon(icons.CLEAR_ALL)]))

        #! ======================================================== Row4 (chat-gpt output text) ==================================================
        self.output_topic = TextField(value="",read_only=True,max_length=280,multiline=True,width=page.width - 20,rtl=True,visible=False,focused_border_color=colors.BLUE_800,border_color="#36618e")

        #! ======================================================== Arcticture of the application ==================================================
        self.row0 = Row([self.tweets_counter,self.number_of_letters,self.time_gap],alignment=MainAxisAlignment.CENTER)
        self.row1 = Row([self.input_topic,],alignment=MainAxisAlignment.CENTER)
        self.row2 = Row([self.link_or_notlink],alignment=MainAxisAlignment.CENTER)
        self.row3 = Row([self.cancel_tweeting,self.re_use_images],alignment=MainAxisAlignment.CENTER)
        self.row4 = Row([self.image_post,self.Video],alignment=MainAxisAlignment.CENTER)
        self.row5 = Row([self.output_topic],alignment=MainAxisAlignment.START)
        self.null = Row([Text("")])
        #! ======================================================== Container and Column that build application ==================================================
        column = Column([self.null,self.row0,self.null,self.row1,self.null,self.row2,self.null,self.row3,self.null,self.row5,self.row4,self.snackbar],spacing=5)
        self.container = Container(content=column)
        self.controls = [self.container]
        page.overlay.append(pick_files_dialog)
        


def Main(page:Page):
    def Drawer_history():
        try:
            end_drawer.controls = [
            Row([Text("سجل التغريدات",size=35,font_family="Andalus")],alignment=MainAxisAlignment.CENTER),
            Row([ElevatedButton("مسح الكل",on_click=lambda e:History_delete(),icon=icons.DELETE_FOREVER),
                 ElevatedButton("تحديث",on_click=lambda e:Drawer_history(),icon=icons.UPDATE_ROUNDED)],alignment=MainAxisAlignment.CENTER),
                 Divider(leading_indent=10,trailing_indent=10,thickness=2,height=10)
        ]
            history_list = History.read_history()
            for x in range(len(history_list)):
                end_drawer.controls.append(Row([TextField(value=history_list[x],text_align=TextAlign.CENTER,border=InputBorder.NONE,read_only=True,width=290,rtl=True,focused_border_color=colors.BLUE_800,border_color="#36618e")],alignment=MainAxisAlignment.CENTER))
                end_drawer.controls.append(Divider(leading_indent=10,trailing_indent=10,thickness=2,height=40))
            end_drawer.update()
            page.update()
        except TypeError:
            pass

        
    
    def History_delete():
        History.Delete_history()
        end_drawer.controls = [
            Row([Text("سجل التغريدات",size=35,font_family="Andalus")],alignment=MainAxisAlignment.CENTER),
            Row([ElevatedButton("مسح الكل",on_click=lambda e: History_delete(),icon=icons.DELETE_FOREVER),
                 ElevatedButton("تحديث",on_click=lambda e: Drawer_history(),icon=icons.UPDATE_ROUNDED)],alignment=MainAxisAlignment.CENTER),
                 Divider(leading_indent=10,trailing_indent=10,thickness=2,height=10)
        ]
        end_drawer.update()
        page.update()

    end_drawer = NavigationDrawer(   
        elevation=9,
        rtl=True,
        open=False,
        position=NavigationDrawerPosition.END,
        tile_padding=20,
        controls=[
            Row([Text("سجل التغريدات",size=35,font_family="Andalus")],alignment=MainAxisAlignment.CENTER),
            Divider(leading_indent=10,trailing_indent=10,thickness=2,height=10),
            Row([ElevatedButton("مسح الكل",tooltip="مسح السجل بالكامل",on_click=lambda e:History_delete(),icon=icons.DELETE_FOREVER),
                 ElevatedButton("تحديث",tooltip="تحديث لسجل التغريدات التي تم ادخالها",on_click=lambda e:Drawer_history(),icon=icons.UPDATE_ROUNDED)],alignment=MainAxisAlignment.CENTER),
                 Divider(leading_indent=10,trailing_indent=10,thickness=2,height=10)
        ],
        )

    mode = IconButton(icon=icons.DARK_MODE,on_click=lambda _: Mode.theme_changed(page=page,Button=mode))
    page.appbar = AppBar(rtl=True,leading=IconButton(icon=icons.HISTORY,on_click= lambda _: page.open(end_drawer)),
        actions=[mode,IconButton(icon=icons.EXIT_TO_APP,tooltip="الخروج من التطبيق",on_click=lambda e: page.window.destroy()),],
        title=Text("تغريدات",size=35,font_family="Andalus"),
        elevation=100)
    
    page.drawer = end_drawer
    page.add(Window_1(page),end_drawer)
    Mode.load(page,mode)
    Drawer_history()
    page.update()

app(Main)