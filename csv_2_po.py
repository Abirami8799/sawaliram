import fire
import os 
import subprocess       


CONTENT_LANGUAGES = [
    ('bn', 'বাংলা'),
    ('en', 'English'),
    ('hi', 'हिंदी'),
    ('mr', 'मराठी'),
    ('ml', 'മലയാളം'),
    ('ta', 'தமிழ்'),
    ('te', 'తెలుగు'),
]

location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


langs = ['bn', 'hi', 'mr', 'ml', 'ta', 'te']


def convert_csv_to_po(app, lang):
    if app == 'public_website':
        locale_dir = os.path.abspath(os.path.join(location, "public_website/locale/"))
    elif app == 'dashboard':
        locale_dir = os.path.abspath(os.path.join(location, "dashboard/locale/"))
    elif app == "sawaliram_auth":
        locale_dir = os.path.abspath(os.path.join(location, "sawaliram_auth/locale/"))

    else:
        raise Exception("Please enter valid app name of sawaliram project")

    if not os.path.exists(locale_dir):
        raise Exception("Please generate PO files first!")
 
    if lang in langs:
        current_dir = os.path.abspath(os.path.join(location, locale_dir+"/"+ lang + "/LC_MESSAGES"))
        com = "csv2po django-"+lang+".csv django.po"
        subprocess.run(com, cwd=current_dir,shell=True)
        
    elif lang == "all":
        for i in langs:
            current_dir = os.path.abspath(os.path.join(location, locale_dir+"/"+ i + "/LC_MESSAGES"))
            com = "csv2po django-"+i+".csv django.po"
            subprocess.run(com, cwd=current_dir,shell=True)

    else:
        raise Exception("Please enter valid language code")
    
    print(">>>  Mission completed all CSV files converted to PO!   <<<")


if __name__ == "__main__":
    fire.Fire(convert_csv_to_po)

# python3 csv_2_po.py public_website all
# python3 csv_2_po.py dashboard all
# python3 csv_2_po.py sawaliram_auth all
