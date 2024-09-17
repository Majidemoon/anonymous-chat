from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)



class Button:
    # Button menu start bot
    def menu_start(self):
        start_button = ReplyKeyboardMarkup(
            [
                ['🔗 به یه ناشناس وصلم کن!'],
                ['💰 سکه', '👤 پروفایل'],
                ['📩 لینک ناشناس من', '📬 انتقادات و پیشنهادات'],
                ['🚸 معرفی به دوستان (سکه رایگان)']
            ],
            resize_keyboard=True
        )
        return start_button
    # Button menu choices chat
    def menu_chatـrequest(self):
        inline_keybord = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('🎲جستجوی شانسی🎲', callback_data='chancesearch')],
                [InlineKeyboardButton('👩‍🦰جستجوی دختر', callback_data='girlsearch'),InlineKeyboardButton('🧑جستجوی پسر', callback_data='boysearch') ],
                [InlineKeyboardButton('جستجوی🌈', callback_data='lgbtsearch')],
                [InlineKeyboardButton('🏠جستجوی اطراف🏠', callback_data='homesearch')]
            ]
        )
        return inline_keybord
    
    #Button menu for display and edit profile
    def menu_profile(self):
        inline_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('📝ویرایش اطلاعات پروفایل', callback_data='editprofile')],
                [InlineKeyboardButton('بلاک لیست🚫', callback_data='blocklist'), InlineKeyboardButton('👥مخاطبین بزودی...', callback_data='soon')]
            ]
        )
        return inline_keyboard
    
    # Button menu for edit profile 
    def menu_edit_profile(self):
        inline_keyborad = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('✏️تغییر نام', callback_data='namechange'), InlineKeyboardButton('✏️تغییر سن', callback_data='agechange')],
                [InlineKeyboardButton('✏️تغییر شهر', callback_data='citychange'), InlineKeyboardButton('✏️تغییر استان', callback_data='provincechange')],
                [InlineKeyboardButton('✏️تغییر جنسیت', callback_data='genderchange'), InlineKeyboardButton('✏️تغییر عکس', callback_data='picturechange')],
                [InlineKeyboardButton('✏️تغییر بیوگرافی', callback_data='biographychange')],
                [InlineKeyboardButton('🔙 بازگشت به منو قبلی', callback_data='backmenuprofile')]
            ]
        )
        return inline_keyborad
    def menu_number(self):
        keyborad_button = ReplyKeyboardMarkup(
            [
                ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"],
                ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29"],
                ["30", "31", "32", "33", "34", "35", "36", "37", "38", "39"],
                ["40", "41", "42", "43", "44", "45", "46", "47", "48", "49"],
                ["50", "51", "52", "53", "54", "55", "56", "57", "58", "59"],
                ["60", "61", "62", "66", "67", "68"]
            ],resize_keyboard=True
        )
        return keyborad_button
    # list provinces for button 
    def menu_provinces(self):
        keboard_button =ReplyKeyboardMarkup(
            [
                ["آذربایجان شرقی", "آذربایجان غربی", "اردبیل"],
                ["ایلام", "بوشهر", "تهران", "چهارمحال و بختیاری"],
                ["خراسان رضوی", "خوزستان", "زنجان", "سمنان"],
                ["سیستان و بلوچستان", "فارس", "قزوین", "کردستان"],
                ["کرمان", "کرمانشاه", "گلستان", "گیلان"],
                ["لرستان", "مرکزی", "هرمزگان", "همدان", "یزد"],
                ["قم", "خراسان شمالی", "خراسان جنوبی", "البرز"],
                ["اصفهان", "مازندران", "کهگیلویه و بویراحمد"]
            ],resize_keyboard=True

        )
        return keboard_button
    # menu city
    def menu_city(self, provinces):
        if provinces == "آذربایجان شرقی":

            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["اسکو", "چاراویماق", "سراب", "بناب", "تبریز",],
                    ["شبستر", "عجب‌شیر", "کلیبر", "میانه", "ورزقان"],
                    ["هادی‌شهر", "تیکمه‌داش", "سروستان", "ایلخچی", "اهر"],
                    ["مراغه", "مرند", "ملکان","بستان‌آباد", "جلفا"],
                    ["کاج", "قره‌آغاج", "کاندو", "خداآفرین"]
                ]
            )

        elif provinces == "آذربایجان غربی":
            keyboard_button =ReplyKeyboardMarkup(
                [
                    ["ارومیه", "اشنویه", "بوکان", "پیرانشهر", "تکاب"],
                    ["چالدران", "خوی", "سردشت", "سلماس", "شاهین‌دژ"],
                    ["ماکو", "مهاباد", "میاندوآب", "نقده", "سرو"],
                    ["پلدشت", "بازرگان", "آواجیق", "ملکان", "باسمنج"]

                ]
            )
        elif provinces == "اردبیل":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["اردبیل", "بیله‌سوار", "پارس‌آباد", "خلخال", "کوثر"],
                    ["گرمی", "مشگین‌شهر", "نمین", "نیر", "اصلاندوز"],
                    ["عنبران", "فخرآباد", "کلور", "مرادلو"]
                ]
            )
        elif provinces == "کردستان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["سنندج", "قروه", "بیجار", "کامیاران", "دیواندره"],
                    ["سقز", "پیرانشهر", "اورامان", "مریوان", "دلبران"],
                    ["سروآباد", "سرو", "حسن‌آباد", "زریبار"]
                ]
            )

        elif provinces == "اصفهان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["اصفهان", "آران و بیدگل", "اردستان", "اصفهان", "برخوار"],
                    ["بوئین و میاندشت", "تیران و کرون", "چادگان", "خمینی‌شهر", "خوانسار"],
                    ["سمیرم", "شاهین‌شهر و میمه", "شهرضا", "دهاقان", "فریدن"],
                    ["فریدون‌شهر", "فلاورجان", "کاشان", "گلپایگان", "لنجان"],
                    ["مبارکه", "نایین", "نجف‌آباد", "نطنز", "هرند"],
                    ["کوهپایه", "جرقویه سفلی", "جرقویه علیا", "خور و بیابانک", "ورزنه"]
                ]
            )
        elif provinces == "البرز":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["کرج", "فردیس", "نظرآباد", "اشتهارد", "ساوجبلاغ"],
                    ["طالقان", "چهارباغ", "گرمدره"]
                ]
            )
        elif provinces == "ایلام":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["ایلام", "دهلران", "آبدانان", "دره‌شهر"],
                    ["ایوان", "مهران", "ملکشاهی", "بدره"],
                    ["چرداول", "سیروان", "هلیلان"]
                ]
            )
        elif provinces == "بوشهر":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["بوشهر", "گناوه", "دشتستان", "دشتی"],
                    ["کنگان", "دیر", "تنگستان", "جم"],
                    ["دیلم", "عسلویه", "بندر ریگ"]
                ]
            )
        elif provinces == "تهران":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["تهران", "ری", "شمیرانات", "اسلامشهر", "شهریار"],
                    ["ورامین", "پاکدشت", "رباط‌کریم", "دماوند", "بهارستان"],
                    ["ملارد", "قدس", "قرچک", "فیروزکوه", "پیشوا"]
                ]
            )
        elif provinces == "چهارمحال و بختیاری":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["شهرکرد", "بروجن", "فارسان", "لردگان"],
                    ["اردل", "کیار", "سامان", "کوهرنگ"],
                    ["بن", "خانمیرزا", "فلارد"]
                ]
            )
        elif provinces == "خراسان جنوبی":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["بیرجند", "قائن", "طبس", "فردوس"],
                    ["نهبندان", "سربیشه", "درمیان", "بشرویه"],
                    ["خوسف", "زیرکوه", "سرایان"]
                ]
            )
        elif provinces == "خراسان رضوی":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["مشهد", "نیشابور", "سبزوار", "تربت‌حیدریه"],
                    ["کاشمر", "تربت‌جام", "قوچان", "خواف"],
                    ["سرخس", "چناران", "گناباد", "تایباد"],
                    ["بجستان", "درگز", "بردسکن", "فریمان"],
                    ["کلات", "خلیل‌آباد", "رشتخوار", "زاوه"],
                    ["طرقبه", "شاندیز"]
                ]
            )
        elif provinces == "خراسان شمالی":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["بجنورد", "شیروان", "اسفراین", "فاروج"],
                    ["جاجرم", "مانه و سملقان", "گرمه", "راز و جرگلان"]
                ]
            )
        elif provinces == "خوزستان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["اهواز", "آبادان", "دزفول", "خرمشهر", "مسجدسلیمان"],
                    ["شوشتر", "بندرماهشهر", "شادگان", "اندیمشک", "ایذه"],
                    ["رامهرمز", "بندر امام خمینی", "بهبهان", "هندیجان", "شوش"],
                    ["رامشیر", "حمیدیه", "باغ‌ملک", "هویزه", "کارون"],
                    ["باوی", "دشت‌آزادگان", "گتوند", "لالی", "آغاجاری"]
                ]
            )
        elif provinces == "زنجان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["زنجان", "خرمدره", "ابهر", "سلطانیه"],
                    ["طارم", "ماه‌نشان", "ایجرود", "خدابنده"],
                    ["سجاس‌رود", "حلب"]
                ]
            )
        elif provinces == "سمنان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["سمنان", "شاهرود", "دامغان", "گرمسار"],
                    ["مهدی‌شهر", "سرخه", "آرادان", "میامی"]
                ]
            )
        elif provinces == "سیستان و بلوچستان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["زاهدان", "چابهار", "ایرانشهر", "زابل"],
                    ["خاش", "سراوان", "سرباز", "نیک‌شهر"],
                    ["کنارک", "زهک", "هیرمند", "فنوج"],
                    ["قصرقند", "دلگان", "مهرستان", "نیمروز"],
                    ["میرجاوه", "سیب و سوران", "بمپور", "راسک"],
                    ["محمد‌آباد", "بزمان", "شهرکی و ناروئی"]
                ]
            )

        elif provinces == "فارس":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["شیراز", "مرودشت", "لارستان", "جهرم", "کازرون"],
                    ["فسا", "داراب", "ممسنی", "نی‌ریز", "آباده"],
                    ["فیروزآباد", "اقلید", "زرین‌دشت", "خرم‌بید", "قیروکارزین"],
                    ["لامرد", "خنج", "سپیدان", "مهر", "پاسارگاد"],
                    ["بوانات", "رستم", "ارسنجان", "بیضا", "سروستان"],
                    ["کوار", "گراش", "زرین‌دشت", "زرقان"]
                ]
            )

        elif provinces == "قزوین":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["قزوین", "البرز", "آبیک", "تاکستان"],
                    ["بویین‌زهرا", "آوج"]
                ]
            )

        elif provinces == "قم":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["قم"]
                ]
            )
        elif provinces == "کرمان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["کرمان", "رفسنجان", "جیرفت", "بم"],
                    ["زرند", "سیرجان", "شهر بابک", "عنبرآباد"],
                    ["کهنوج", "رودبار جنوب", "ریگان", "قلعه گنج"],
                    ["بردسیر", "فهرج", "بافت", "ارزوئیه"],
                    ["منوجان", "نرماشیر", "فاریاب", "راور"],
                    ["انار", "ماهان", "کشکوئیه", "هجدک"],
                    ["گلباف", "راین", "جوپار", "خورسند"]
                ]
            )
        elif provinces == "کرمانشاه":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["کرمانشاه", "اسلام‌آباد غرب", "هرسین", "سنقر"],
                    ["سرپل ذهاب", "قصر شیرین", "جوانرود", "پاوه"],
                    ["ثلاث باباجانی", "دالاهو", "کنگاور", "صحنه"],
                    ["روانسر", "گیلانغرب"]
                ]
            )
        elif provinces == "کهگیلویه و بویراحمد":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["یاسوج", "دوگنبدان", "دهدشت", "لیکک"],
                    ["باشت", "چرام", "لنده", "دیشموک"]
                ]
            )
        elif provinces == "گلستان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["گرگان", "گنبد کاووس", "علی‌آباد کتول", "مینودشت"],
                    ["آق‌قلا", "کردکوی", "بندر ترکمن", "کلاله"],
                    ["گمیشان", "مراوه‌تپه", "آزادشهر", "رامیان"],
                    ["بندر گز", "فاضل آباد", "گالیکش"]
                ]
            )
        elif provinces == "گیلان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["رشت", "بندر انزلی", "لاهیجان", "لنگرود"],
                    ["آستانه اشرفیه", "رودسر", "رودبار", "فومن"],
                    ["صومعه‌سرا", "تالش", "رضوانشهر", "ماسال"],
                    ["شفت", "املش", "سیاهکل", "آستارا"],
                    ["خشکبیجار", "بندر کیاشهر", "چابکسر"]
                ]
            )

        elif provinces == "لرستان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["خرم‌آباد", "بروجرد", "دورود", "کوهدشت"],
                    ["الیگودرز", "نورآباد", "ازنا", "الشتر"],
                    ["پلدختر", "سراب دوره", "معمولان", "چغلوندی"],
                    ["ویسیان", "زاغه"]
                ]
            )
        elif provinces == "مازندران":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["ساری", "بابل", "آمل", "قائم‌شهر"],
                    ["نوشهر", "چالوس", "بهشهر", "رامسر"],
                    ["بابلسر", "تنکابن", "جویبار", "نور"],
                    ["محمودآباد", "فریدون‌کنار", "گلوگاه", "نکا"],
                    ["عباس‌آباد", "سوادکوه", "کلاردشت", "سوادکوه شمالی"],
                    ["سیمرغ", "میاندورود", "زیرآب", "کجور"]
                ]
            )
        elif provinces == "مرکزی":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["اراک", "ساوه", "خمین", "محلات"],
                    ["تفرش", "آشتیان", "دلیجان", "شازند"],
                    ["زرندیه", "کمیجان", "خنداب", "فرمهین"],
                    ["میلاجرد", "نوبران"]
                ]
            )
        elif provinces == "هرمزگان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["بندرعباس", "قشم", "کیش", "بندر لنگه"],
                    ["میناب", "بستک", "رودان", "جاسک"],
                    ["حاجی‌آباد", "ابوموسی", "خمیر", "سیریک"],
                    ["پارسیان", "کنگ"]
                ]
            )

        elif provinces == "همدان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["همدان", "ملایر", "نهاوند", "اسدآباد"],
                    ["تویسرکان", "کبودرآهنگ", "رزن", "فامنین"],
                    ["بهار", "قهاوند", "لالجین", "سامن"]
                ]
            )
        elif provinces == "یزد":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["یزد", "میبد", "اردکان", "بافق"],
                    ["مهریز", "ابرکوه", "تفت", "خاتم"],
                    ["اشکذر", "هرات", "بهاباد", "فهرج"]
                ]
            )
        elif provinces == "سیستان و بلوچستان":
            keyboard_button = ReplyKeyboardMarkup(
                [
                    ["زاهدان", "چابهار", "ایرانشهر", "زابل"],
                    ["خاش", "سراوان", "سرباز", "نیک‌شهر"],
                    ["کنارک", "زهک", "هیرمند", "فنوج"],
                    ["قصرقند", "دلگان", "مهرستان", "نیمروز"],
                    ["میرجاوه", "سیب و سوران", "بمپور", "راسک"],
                    ["محمد‌آباد", "بزمان", "شهرکی و ناروئی"]
                ]
            )

        return keyboard_button

    # menu gender 
    def menu_gender(self):
        keyboard_button = ReplyKeyboardMarkup(
            [
                ['پسر', 'دختر']
            ],resize_keyboard=True
        )
        return keyboard_button
    #menu send request user to user 
    def menu_direct_message(self):
        inline_keybord = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('ارسال پاسخ', 'sendanswer'), InlineKeyboardButton('بلاک', 'blocksenddirect')]
            ]
        )
        return inline_keybord
    # menu show profile and end chat
    def menu_show_pro_end_caht_active(self):
        keyboard_button = ReplyKeyboardMarkup(
            [
                ['نمایش پروفایل'],
                ['فعال سازی چت خصوصی'],
                ['پایان چت']
            ], resize_keyboard=True
        )
        return keyboard_button
    def menu_show_pro_end_caht_inactive(self):
        keyboard_button = ReplyKeyboardMarkup(
            [
                ['نمایش پروفایل'],
                ['غیرفعال سازی چت خصوصی'],
                ['پایان چت']
            ], resize_keyboard=True
        )
        return keyboard_button
    #menu show profile 
    def munu_show_profile(self):
        inline_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('درخواست چت', 'chatrequestofuser'), InlineKeyboardButton('بلاک', 'blockuser')],
                [InlineKeyboardButton('پیام دایرکت', 'directmessage'), InlineKeyboardButton('گزارش', 'reportuser')]
            ]
        )
        return inline_keyboard
    # menu block next end chat 
    def menu_block(self):
        inline_keyboard = ReplyKeyboardMarkup(
            [
                ['بلاک کن'],
                ['نه بعدا وصل میشم باز']
            ],resize_keyboard=True
        )
        return inline_keyboard
    
