from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import InputMediaPhoto
import requests
from telegram import InputMediaPhoto
from io import BytesIO


TOKEN = "8151600770:AAE4TCfk9By5tex-L32ByOtl2XXnG3Pe9VE"

AUDIO_FILES = {
    "3 курс": {
        "Unit 1": {
            "Conversation and discussion": {
                "audio": "https://drive.google.com/uc?id=1rKn8YjTwrC1bHWVCdhVYgGq6cTqTdG68&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1fIcYIuSUzpvdSbi4N4ZLFmgoROMPfdvl" ,
                "https://drive.google.com/uc?export=view&id=1mIVr_gYtUCK_R0VAUCPFs6n0gZH4v6MT" , 
                "https://drive.google.com/uc?export=view&id=1S8G2DfcbZ2LYiQG-MQvGeWMUS9SDUHs0" ,
                "https://drive.google.com/uc?export=view&id=1oYlro59tSmNJefk4Dte_t3Zl_-rJMGur" ,
                "https://drive.google.com/uc?export=view&id=1-oVzy9muKp6BIdMAiNwX583gyQyJDRqz"

                ]
                
            },
            "Essential Vocabulary 1": {
                "audio": "https://drive.google.com/uc?id=163nYAZFy1NgbQ258N82LmsDxw5F_Z5RH&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1Lx8rmcfN98Cm4nwf8XTVwgBeLdyzgQIm" ,
                "https://drive.google.com/uc?export=view&id=1U9f9Y5kpwOqbfD3osWhI7R1QraC5cEhu" ,
                "https://drive.google.com/uc?export=view&id=1IcTje6M_-ugnz06dSx_7NdsVf4c52BP2" ,
                "https://drive.google.com/uc?export=view&id=1zuWeTVSlPfJ78TJf8_KuVuxdBLGQjAhm" ,
                "https://drive.google.com/uc?export=view&id=17ZtTf2K2Hd9_1ixDRNV56VTztIg7FVWH" ,
                "https://drive.google.com/uc?export=view&id=1Ir_NrrvVo60G_ot7l2VV5O1vI6kXpq92" ,
                "https://drive.google.com/uc?export=view&id=1vwDgaCXUiDGT-WbbE9aHbshWRmNmsYNB" ,
                "https://drive.google.com/uc?export=view&id=1gfsPeLKCEL4hdTdTNYYbJK4a0yvWnneX"

                ]

    
            },
            "Essential Vocabulary 2": {
                "audio": "https://drive.google.com/uc?id=1A34tk8cH1r5MKrPfTyvAPCjLYkO0nznb&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1Lx8rmcfN98Cm4nwf8XTVwgBeLdyzgQIm" ,
                "https://drive.google.com/uc?export=view&id=1U9f9Y5kpwOqbfD3osWhI7R1QraC5cEhu" ,
                "https://drive.google.com/uc?export=view&id=1IcTje6M_-ugnz06dSx_7NdsVf4c52BP2" ,
                "https://drive.google.com/uc?export=view&id=1zuWeTVSlPfJ78TJf8_KuVuxdBLGQjAhm" ,
                "https://drive.google.com/uc?export=view&id=17ZtTf2K2Hd9_1ixDRNV56VTztIg7FVWH" ,
                "https://drive.google.com/uc?export=view&id=1Ir_NrrvVo60G_ot7l2VV5O1vI6kXpq92" ,
                "https://drive.google.com/uc?export=view&id=1vwDgaCXUiDGT-WbbE9aHbshWRmNmsYNB" ,
                "https://drive.google.com/uc?export=view&id=1gfsPeLKCEL4hdTdTNYYbJK4a0yvWnneX"

                ]
            },
            "Speech Patterns": {
                "audio": "https://drive.google.com/uc?id=1kR2usW6LY0aVoDHsRjyAgv41vPv0lAPx&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=18KUpt8TustGyG3XUhk1abi8VFIHfKvrF" ,
                "https://drive.google.com/uc?export=view&id=1pEzfiNeqAxcTLxQPPao43op3gec3wYE8" ,
                "https://drive.google.com/uc?export=view&id=1jr-vSDR3BQY5GMppVRe21RXHaZyF9BFg" ,
                "https://drive.google.com/uc?export=view&id=1DzGo13jTHAzg1pH5CBrndiGM9dVF6XJo" ,
                "https://drive.google.com/uc?export=view&id=1BplLxJZifzmyi_JEn66jLbfXI0XOfVpA" , 
                "https://drive.google.com/uc?export=view&id=1CfgtoO8fMFFlaQz75nMn8QQ1ugaX3t1R" ,
                "https://drive.google.com/uc?export=view&id=1-kjCqtjCevbXAEdgUNVFt8rg4AAAQA6O"
                ]
            },
            "Word Combinations": {
                "audio": "https://drive.google.com/uc?id=1r6wLRw1krxfpeYSUUcs5xFkjmii_1ckI&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=18aWI5s-rqCTWH42D4xRlo5xqIvV-xdYi",
                "https://drive.google.com/uc?export=view&id=1fxe9l7IgLZF6rhRsPEeHA-v29k5McS8j"
                
                ]
            },
            "Quizlet": {
                "text_doc": """Quizlet:  
                \n\n Quizlet: Unit 1 Essential vocabulary (https://quizlet.com/ru/823453888/ar-unit-1-essential-vocabulary-flash-cards/?funnelUUID=282dfe6d-25a0-4642-970d-a3b8a9eecd8c)
                \n\n Quizlet: Unit 1 (https://quizlet.com/ru/822995389/ar3-unit-1-flash-cards/?funnelUUID=67f0efbf-94cd-45f6-aaf2-ddf1005bc947)
                \n\n Quizlet: Unit 1 Topical Vocabulary (https://quizlet.com/ru/828608167/ar3-unit-1-topical-vocabulary-flash-cards/?funnelUUID=3098c6e9-05e9-42c8-8c38-35c357c3e32d)"""
                }
            
        },
        "Unit 2": {
            "Conversation and discussion": {
                "audio": "https://drive.google.com/uc?id=13kiN21DKuJYjO75QPX1WpCpGp6OK1pu9&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1346fEc8waJgi_I2oa8bxejbv-6FR85zX" ,
                "https://drive.google.com/uc?export=view&id=1syw839rR7_uNBFS0mcHxRiVnZuyh7uA8" ,
                "https://drive.google.com/uc?export=view&id=17OvYtc2JvqOpzLorTXQQXJkJVSNLTfUx" ,
                "https://drive.google.com/uc?export=view&id=14p_VmYL-q3zN-duBVzAvap6kqxdYSWt4" ,
                "https://drive.google.com/uc?export=view&id=14emByJT57yQLMdHfvMysg2eazp85K6C-" ,
                "https://drive.google.com/uc?export=view&id=1kCNtQ4kiNuTR3hLkYUZ1ngnibteLKNHF" ,
                "https://drive.google.com/uc?export=view&id=1L2W-MuR86uvmWqeuS9kpMSuLNUwqwcYi"

                ]
                
            },
            "Essential Vocabulary 1": {
                "audio": "https://drive.google.com/uc?id=1ARjkedd1XmUU7vgd492hHHMh-H42w8tx&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1cXgmxYFjC4SsKTcO2f5HbGEb_CJSrn3y" ,
                "https://drive.google.com/uc?export=view&id=1QwM-ObxCNzLvca4XW3hh_Rgjf0HO8_YB" ,
                "https://drive.google.com/uc?export=view&id=1fpLxgBgJPdjtbDZorH3jRXzJp58kdjL6" ,
                "https://drive.google.com/uc?export=view&id=1Cu_e3kqqQ31WmIyWF82nRJAo6HdHWsZ8" ,
                "https://drive.google.com/uc?export=view&id=1s9DEazRYMvvCZwYlhMskqmzZQBN_SQkv" ,
                "https://drive.google.com/uc?export=view&id=1o9qqAOXwT4Zu7ajf9jTZDTbwNIAIoNky" ,
                "https://drive.google.com/uc?export=view&id=1BK38HGge-7J-03Z8eMnEYZ6_Dqx-twiU" ,
                "https://drive.google.com/uc?export=view&id=1uKYwyaf_EuJySBwUc2SOlB0xTPRl6TZy" 

                ]
                
            },
            "Essential Vocabulary 2": {
                "audio": "https://drive.google.com/uc?id=1fK0d8RDEFly8ERa4HkCnunCGyWSxgBv-&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1cXgmxYFjC4SsKTcO2f5HbGEb_CJSrn3y" ,
                "https://drive.google.com/uc?export=view&id=1QwM-ObxCNzLvca4XW3hh_Rgjf0HO8_YB" ,
                "https://drive.google.com/uc?export=view&id=1fpLxgBgJPdjtbDZorH3jRXzJp58kdjL6" ,
                "https://drive.google.com/uc?export=view&id=1Cu_e3kqqQ31WmIyWF82nRJAo6HdHWsZ8" ,
                "https://drive.google.com/uc?export=view&id=1s9DEazRYMvvCZwYlhMskqmzZQBN_SQkv" ,
                "https://drive.google.com/uc?export=view&id=1o9qqAOXwT4Zu7ajf9jTZDTbwNIAIoNky" ,
                "https://drive.google.com/uc?export=view&id=1BK38HGge-7J-03Z8eMnEYZ6_Dqx-twiU" ,
                "https://drive.google.com/uc?export=view&id=1uKYwyaf_EuJySBwUc2SOlB0xTPRl6TZy" 

                ]
            },
            "Speech Patterns": {
                "audio": "https://drive.google.com/uc?id=1-JNZng1VC3Q9XDQtXGC5aJj4Zk-CbpOG&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1M3ifiCqtiHGnkUAslO5YB_IWr85W2Xy9" ,
                "https://drive.google.com/uc?export=view&id=1HW_YJ8vc0MWsB3sMAQEhm-JGgf_vgn8R" ,
                "https://drive.google.com/uc?export=view&id=1WvDVB5a9KNPmAFIaVUkipKbCY0F9rbXI" ,
                "https://drive.google.com/uc?export=view&id=15yf-PwoOyI5WljnMA_k8i9zEL80OZQAj" ,
                "https://drive.google.com/uc?export=view&id=13LNxuJk4wSFZWHCI7mXpJ-4dMyrCFZ_D" ,
                "https://drive.google.com/uc?export=view&id=14_wWIwUVbn4pGU3kF3JlvlOdGOK3SUcX" 

                ]
                
            },
            "Word Combinations": {
                "audio": "https://drive.google.com/uc?id=1DfaT4ABmQkwDsyAz9fufYZmExl52FeDv&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1iY_02WP8nzK6BJZhjf_YQ90PPkgp2nfi",
                "https://drive.google.com/uc?export=view&id=1nx1LUgW8pY8RMIr8RhiPKxBeEKasaLnZ"
                ]

            },
            "Quizlet": {
                "text_doc": """Quizlet:  
                \n\n Quizlet: Unit 2 Essential Vocabulary (https://quizlet.com/ru/833634988/ar-3-unit-2-essential-vocabulary-flash-cards/?funnelUUID=f68835cc-86d0-453a-ba7b-9559e80591cf)   
                \n\n Quizlet: Unit 2 Topical Vocabulary (https://quizlet.com/ru/837862382/3-ar-unit-2-topical-vocabulary-flash-cards/?funnelUUID=3f84f401-bbe0-4b76-9770-4d891054975f)"""
                
                }
        },
        "Unit 3": {
            "Conversation and discussion": {
                "audio": "https://drive.google.com/uc?id=1zi4px5zR8tAEGq8d9QCSBGxX3XoxgOvc&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1ndaqrZ0VyY0clxziStgOeWz9QRxNAFbx",
                "https://drive.google.com/uc?export=view&id=1z4w0PurFCB5jDMfIbGex46PX4Tf3Ie5u",
                "https://drive.google.com/uc?export=view&id=1VetsMivm5eF9lgLMOxMtCEtXf0_BDQFB",
                "https://drive.google.com/uc?export=view&id=12H-Hw43mC_ZB1HKuSqDICS636aciZOuK",
                "https://drive.google.com/uc?export=view&id=1etfpW8z1JD_d4IA3vgr5JFoPaM0_jR9W",
                "https://drive.google.com/uc?export=view&id=1vICenc-iMwU6REjgqmSYAOgjsPQY-72K",
                "https://drive.google.com/uc?export=view&id=19OE8v6uT_GE6L4l5qPlc7Kwvgpkx5RQw",
                "https://drive.google.com/uc?export=view&id=1nEdqp4ysPKvwZkr7LLBCX_GuE8D5onfz"
                ]
                
            },
            "Essential Vocabulary 1": {
                "audio": "https://drive.google.com/uc?id=17VpAQK2iu8n4g4uPWvnaworaLDOk4QxO&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1zwJlgXhCTYEohezqRkea0JAFQ_lkvykC",
                "https://drive.google.com/uc?export=view&id=1L73agin19OmH4MzSkq0sC6EpXPO-7Yzo",
                "https://drive.google.com/uc?export=view&id=1p2QEXpEjftjw7hpK-CauOgizLG6Ke0Qh",
                "https://drive.google.com/uc?export=view&id=1Z8TB0mCtMIYrPTFRK7Ax_IOFTsTTlpft",
                "https://drive.google.com/uc?export=view&id=1QyQCr1XzJuCW11Fp5dnav86dkZqqshfX",
                "https://drive.google.com/uc?export=view&id=1AdMZsC2JrOwJ4WPkqTahLTIRkehZ6jhx",
                "https://drive.google.com/uc?export=view&id=1M9cqH1dDvRqWhGlEaRDNGy2wc2q3xVIE",
                "https://drive.google.com/uc?export=view&id=16G8JdtIdynFwsaLwNsPlcFH7IBlUjtGA",
                "https://drive.google.com/uc?export=view&id=1abLf3_jR-wvfPEn0reuzyLi9bA-vjzdn"
                ]
                
            },
            "Essential Vocabulary 2": {
                "audio": "https://drive.google.com/uc?id=1WCExAVXWOhK89myoYeVnM_rTvOM2tIV4&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1zwJlgXhCTYEohezqRkea0JAFQ_lkvykC",
                "https://drive.google.com/uc?export=view&id=1cdqAulFd_zpBdi8MWXt-ikpoeqjgUWna",
                "https://drive.google.com/uc?export=view&id=1Gh5P5U46kLIcaEG12RHLDSO_rlcJ0RSU",
                "https://drive.google.com/uc?export=view&id=1X8IS0lU_tLqW4g98TjC5PJh5kCbLcZ_P",
                "https://drive.google.com/uc?export=view&id=1kjPi7bgUCgw-2FLA_7NIBFVGQ8TpWwfw",
                "https://drive.google.com/uc?export=view&id=1vYLU6j-XNHSoIz-R5SESRMMNE0E7_17i"
                ]
                
            },
            "Speech Patterns": {
                "audio": "https://drive.google.com/uc?id=1Mr-s0SethwGhKazI0Ad5tMQLIBO6bZzr&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=11-7pHvaFOTK4cCJg6trxgPIJN4PLS3_r",
                "https://drive.google.com/uc?export=view&id=1rT4hwglnd20Q_ux9GK19EWI_j6Cfm20g",
                "https://drive.google.com/uc?export=view&id=1VFmZVdWiQxlgDID2EakB4Gsdp5D4-ShN",
                "https://drive.google.com/uc?export=view&id=1YIKspQ0oB1LelUOvLq5oZdm6xrS5g9Ug",
                "https://drive.google.com/uc?export=view&id=1EwUtEH1SeBSNbXkzK9PxSDvBgbeJj7Dt"
                ]
                
            },
            "Word Combinations": {
                "audio": "https://drive.google.com/uc?id=1rrMfrSlnlw5iv8qqCM-LND4Tga5R1UHl&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=15jLy0vLyOvg09gDzAaAOAZTrqFnMiYK2",
                "https://drive.google.com/uc?export=view&id=1zZJpc1XCBBb2ITGMW_oVhWZj1a4u4xjJ"    
                ]
                
            },
            "Quizlet": {
                "text_doc": """Quizlet:  
                \n\n Quizlet: Unit 3 Text vocabulary (https://quizlet.com/ru/963934692/3ar-unit-3-text-new-words-flash-cards/?funnelUUID=88546737-15dc-4d76-a8cd-025680c47383)  
                \n\n Quizlet: Unit 3 Essential Vocabulary (https://quizlet.com/ru/843363219/ar-3-unit-3-essential-vocabulary-flash-cards/?funnelUUID=dc25100e-3063-4b40-858f-802fb9e16d8b)  
                \n\n Quizlet: Unit 3 Topical Vocabulary (https://quizlet.com/ru/847436724/ar-3-unit-3-topical-vocabulary-flash-cards/?funnelUUID=607984c0-ee43-43b3-8125-48a7c0ed0f38)"""
                
                }
        },
        "Unit 4": {
            "Conversation and discussion": {
                "audio": "https://drive.google.com/uc?id=1WKs1WNT4KbxNAbqJokp691NP-COfhsJo&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1cRbikNV1sIOUBx6QZg6KOLj6U449XPAy",
                "https://drive.google.com/uc?export=view&id=1moRIed9ezj_f-lFMbIf6PViAccqu52nx",
                "https://drive.google.com/uc?export=view&id=11De0GUvZDTxL-vs0fDp_49cVxFkAmfZe",
                "https://drive.google.com/uc?export=view&id=1Kzyj0ch3QgoXTXE7nCTPWgaMPsh_OgUb",
                "https://drive.google.com/uc?export=view&id=1Lz2o7Mou8eQ5VMGyrCIKsmbGwj555EQN",
                "https://drive.google.com/uc?export=view&id=1-jT5mVF0w4yRa4BFMOO4DZuxP1ObZyM2",
                "https://drive.google.com/uc?export=view&id=1E0uAzDkiT7UpnK0N0jG97pKUF-1jiIHl",
                "https://drive.google.com/uc?export=view&id=1GDKUdnV5cUWMt01Cei9rGA-7cxMmmp3M",
                "https://drive.google.com/uc?export=view&id=1NxsLS57QIkpU_k2ftn1LpymuyCJlwdJj"
]
            },
            "Essential Vocabulary 1": {
                "audio": "https://drive.google.com/uc?id=10V6cNUyjeJz6TMNxCt8eg6nte6z1b6p_&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=144N3dto58d02WYi_7pTDRI98uhV7jqHL",
                "https://drive.google.com/uc?export=view&id=1PcON7uthTNbCdrQ6XD3ML3R2AhYNzgcO",
                "https://drive.google.com/uc?export=view&id=1ohle5CCutA0jMKLo-aK1taa8l-ty85Uu",
                "https://drive.google.com/uc?export=view&id=11lJVYKe61LPjLmyqSXdlY1knGOdJDCGI",
                "https://drive.google.com/uc?export=view&id=18ILgBX8AzHesRduoRVHG_Y1dcInK4uzu",
                "https://drive.google.com/uc?export=view&id=19s_yTxFdf4VgceEba0HSzsK2jegL4DNX",
                "https://drive.google.com/uc?export=view&id=1dNEkQqRUqksBMh3dVkMiT5oyQO_1ZK85",
                "https://drive.google.com/uc?export=view&id=1wBImsB1gm1Ba2n0rHLrjea_esWb0QFoT",
                "https://drive.google.com/uc?export=view&id=1by2vSF4ozUQHjcBpLhKR_BY1QTk9k9Uq"
                ]
            },
            "Essential Vocabulary 2": {
                "audio": "https://drive.google.com/uc?id=10V6cNUyjeJz6TMNxCt8eg6nte6z1b6p_&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=144N3dto58d02WYi_7pTDRI98uhV7jqHL",
                "https://drive.google.com/uc?export=view&id=1D8dbLI9UpAu-lEmt5v1TKuJIiaOEBe0-",
                "https://drive.google.com/uc?export=view&id=1I5cflKesxgohUVdCE8oICQG47IDaPSNa",
                "https://drive.google.com/uc?export=view&id=1TpZi3rJNUPEBdzj37PchBiiNxteyn0sQ",
                "https://drive.google.com/uc?export=view&id=1itOD_5aA_LtbgCXNzHaTpt6kxKU2t6dE",
                "https://drive.google.com/uc?export=view&id=1EnNnwP9v81POUjaZYed4ZwwMVVHEoRwT",
                "https://drive.google.com/uc?export=view&id=1YgIJY-MCVJcJHeWDHMKtvOLmHI7URsVp"
                ]
            },
            "Speech Patterns": {
                "audio": "https://drive.google.com/uc?id=1EtIcZJyeNMEm8WCLO16haLg7Db-8PsID&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1Tv30tiCQxBmCDMSCUEEyHhDJMWO--FDA",
                "https://drive.google.com/uc?export=view&id=1-mqPI3eE6HkSC_MDXOqrVkonqVyC_U1f",
                "https://drive.google.com/uc?export=view&id=1Ibpkn8TgR59Q7LA2F5LdU9wJM-bLcDb9",
                "https://drive.google.com/uc?export=view&id=187IGIhsIgEL7zDUo7ul4jfmUD3f3LPg9",
                "https://drive.google.com/uc?export=view&id=1LkZ3JEh-3lcCzU0srT_d0vLJZDk42ggW",
                "https://drive.google.com/uc?export=view&id=1xMFp4AkxlT9LJI4nuU5Xfm6Cfh2BOk_1",
                "https://drive.google.com/uc?export=view&id=10T1_DIV3yw6J3JubBAOgPtg8s8xvkG5f",
                "https://drive.google.com/uc?export=view&id=1DC5xBDXjIB_OhdRpnyykK07fI8ZHTXOF"
                ]
            },
            "Word Combinations": {
                "audio": "https://drive.google.com/uc?id=1dIpTt9hYHQ0DsKPxz4Bw5dEYyNWrQlOE&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1bf1fhh8VHQq0xjSOPNTa2tz1DQdy8hRZ",
                "https://drive.google.com/uc?export=view&id=13Myc8x10BBMMIp8ccbuYMG-ZLnzkb_Kk"
                ]
            },
            "Quizlet": {
                "text_doc": """Quizlet:  
                \n\n Quizlet: Unit 4 Essential Vocabulary (https://quizlet.com/ru/856042444/ar-3-unit-4-essential-vocabulary-flash-cards/?funnelUUID=46871cf9-aa6d-43f9-b204-4717a7710d8f)
                \n\n Quizlet: Unit 4 Topical Vocabulary part 1 (https://quizlet.com/ru/859544817/ar3-unit-4-topical-vocabulary-part-1-flash-cards/?funnelUUID=8b04af76-8850-4cd1-b367-5b845d57c676)
                \n\n Quizlet: Unit 4 Topical vocabulary part 2 (https://quizlet.com/ru/859005305/ar-3-u-4-topical-vocabulary-part-2-flash-cards/?funnelUUID=52661ffe-6971-487a-88cc-490d7fefbe51)"""
                
                }
        },
        "Unit 5": {
            "Conversation and discussion": {
                "audio": "https://drive.google.com/uc?id=1vGrxJPW-RRgYPbziK6HSxzcDtmWKwU07&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1zpRcEiB30gTEF8MQbTs6ONxxS6ALsFfP",
                "https://drive.google.com/uc?export=view&id=1pxjzV56ozjtbgrCY0yIb5n_HHHziIy-W",
                "https://drive.google.com/uc?export=view&id=1aqe3iA5mWFDalb4O57MkikKxBlv88cNz",
                "https://drive.google.com/uc?export=view&id=1YLaEPICGuxHqm4OkSnR4BrzN6PqWg2H3",
                "https://drive.google.com/uc?export=view&id=17DREuX81iDLBelqDtqwemcJKb_3OTc1m",
                "https://drive.google.com/uc?export=view&id=12rbb2wD7PUmT6L5mEzZsrGeTePJW66cr"
                ]
            },
            "Essential Vocabulary 1": {
                "audio": "https://drive.google.com/uc?id=1z2dkB10kA379HXAwEjqJX2HChq4vq_f6&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1ivDAc_EZ1XOHKnPkaX9TfqAAFVTsFIHX",
                "https://drive.google.com/uc?export=view&id=1dA3EA-KXRhWnEZrYb54u5JsyGiv7P-yC",
                "https://drive.google.com/uc?export=view&id=1rXvXfw2EIMy2ilimUnvWmw69OsxQkNeh",
                "https://drive.google.com/uc?export=view&id=10Qj7uNQWiV3EYFJXpZf9k8hTHHEYtLGg",
                "https://drive.google.com/uc?export=view&id=1hLdcu64EaFhfYpmsbsSqu545UGUjtRYF",
                "https://drive.google.com/uc?export=view&id=1PjYCMaw-mcFJy-R-f7xXR9rizeSTqtsU",
                "https://drive.google.com/uc?export=view&id=1GUMvc7PSNdfDWvm3OSTMMh7zpy8r7Ooh",
                "https://drive.google.com/uc?export=view&id=1A59jNz-33sBj8fp_dJbqAu3STABQHLou",
                "https://drive.google.com/uc?export=view&id=1bBHKYeh8Mglqd85iCzm5IPNIZlxOQ-wq"
                ]

            },
            "Essential Vocabulary 2": {
                "audio": "https://drive.google.com/uc?id=1MDacQdtjNRwmTuBIwxATfurYrjbyJE29&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1ivDAc_EZ1XOHKnPkaX9TfqAAFVTsFIHX",
                "https://drive.google.com/uc?export=view&id=18i4agRl4BbrElKt5uNACwGkh8t2A4bJE",
                "https://drive.google.com/uc?export=view&id=1SRGJePXW8UPudr3iOd-KbGJm6aU_5osn"
                ]
            },
            "Speech Patterns": {
                "audio": "https://drive.google.com/uc?id=1vGrxJPW-RRgYPbziK6HSxzcDtmWKwU07&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1OQ1hw5v11nOtDo5Sp1-wG4zhaOnyO-Uv" ,
                "https://drive.google.com/uc?export=view&id=1VT804LpN_Pcv7Onynqm-y5bTnDAxqjN-",
                "https://drive.google.com/uc?export=view&id=1wU0MUCX3vw8gisFas_agVNvXIVHzuGUa",
                "https://drive.google.com/uc?export=view&id=16FzgsPwE3tKEH6imYzEjyMRXwj2QlQBf",
                "https://drive.google.com/uc?export=view&id=19m-T_NaCWAL6LmgLSEN-0AKe1kjt1ecH",
                "https://drive.google.com/uc?export=view&id=1q9hTzFXBNtTy1jRVWSG_YZ1yvOvtq5J5",
                "https://drive.google.com/uc?export=view&id=1Hax_2T-o2I3BIANi5MDmoMeeg7rqLuGF",
                "https://drive.google.com/uc?export=view&id=1BIa-69RB6Xvc8sdb32z2W1oWZnYEqdhl"
                ]
            },
            "Word Combinations": {
                "audio": "https://drive.google.com/uc?id=1jvUEWhMVI7Wh4-Fl4_IgYJrWgYPbxZcL&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1qcP_Zf1qad9z7WRUlgXWs1IKoSPpe5RN" ,
                "https://drive.google.com/uc?export=view&id=1mm6smEdcPlLdgD_kKP8f8sI9qhhqI71R"   
                ]
            },
            "Quizlet": {
                "text_doc": """Quizlet:  
                \n\n Quizlet: Unit 5 Text Essential Vocabulary (https://quizlet.com/ru/879623205/ar-3-unit-5-text-essential-vocabulary-flash-cards/?funnelUUID=37169c9d-a9a6-474a-bf8e-a75507f5992d)
                \n\n Quizlet: Unit 5 Topical Vocabulary (https://quizlet.com/ru/883081325/ar-3-unit-5-topical-vocabulary-flash-cards/?funnelUUID=03c186cf-740c-4b35-a330-4f6c1cffb4ca)
                \n\n Quizlet: Unit 5 Text vocabulary (https://quizlet.com/ru/773498895/unit-5-arakin-text-vocabulary-flash-cards/?funnelUUID=cd6f8245-d9c3-4f17-bac1-052e21837a1a)"""
                }
        },
        "Unit 6": {
            "Conversation and discussion": {
                "audio": "https://drive.google.com/uc?id=1LakfRsf0loK0vkDR6wWA_fr8IPAj4Ya3&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1GdLyjvV-IGITgj-CvYc7YGpfYnXd_ZRY",
                "https://drive.google.com/uc?export=view&id=1-gTn12qAU71ARAZV7n4xxofz2EKHgtqO" ,
                "https://drive.google.com/uc?export=view&id=1TRt2Ky0k-DaRHmoBHwwVRQPGtmsRit3o"    
                ]
            },
            "Essential Vocabulary 1": {
                "audio": "https://drive.google.com/uc?id=11dp18QrkX6R748azLV3aiaoDh5JUhhFG&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1HjBc7tFQSwH16pEDMa52k2LaCEclvoZU",
                "https://drive.google.com/uc?export=view&id=1dLwWHnhdWTaeMUuMhHF5rzsK91Pgy1gn",
                "https://drive.google.com/uc?export=view&id=1Z5LTcRqfROGEqB4HjjT-7ty-YRik6m9t",
                "https://drive.google.com/uc?export=view&id=1ZrDkd-51iz1bRMoGiPMX0Ee35546GxXg",
                "https://drive.google.com/uc?export=view&id=1QmwzZycp3CZ7Z2P7fDMdHf6lgroprSxT"
                ]

            },
            "Essential Vocabulary 2": {
                "audio": "https://drive.google.com/uc?id=1tagAm8ZUcSyiS4PI_hBceBKxwUYLGm7r&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1HjBc7tFQSwH16pEDMa52k2LaCEclvoZU",
                "https://drive.google.com/uc?export=view&id=19JBMpeRTfzewR7P0yYk7llu68ZE8v6yh",
                "https://drive.google.com/uc?export=view&id=1HnHtk6ADOESiyswH38hMbNP9KGDxMHrt",
                "https://drive.google.com/uc?export=view&id=1B1tOkfJeT-1Adc6N1f9061QMKfOd9eqY",
                "https://drive.google.com/uc?export=view&id=14sJCMQciyjyEpZviXJwEi2_S7ZHBTx-A",
                "https://drive.google.com/uc?export=view&id=12BuBNl4V-3CZKacAYL74EaDK-RexIQ7b",
                "https://drive.google.com/uc?export=view&id=1j7-_Jf57VZkXczYHnZ4vNsiSrdMJnJZ2",
                "https://drive.google.com/uc?export=view&id=1wRNsu6wEh2HaEwLdpu0TnGR4NAoaPcn5"
                ]

            },
            "Speech Patterns": {
                "audio": "https://drive.google.com/uc?id=1nZSCfc9jNj7SDvuYvtvuCqr63HQH2Ijm&export=download" ,
                "image": [ 
    
                "https://drive.google.com/uc?export=view&id=19wFtvS-HC73ZpxCe-qOyfy05fCMnI7ad" ,
                "https://drive.google.com/uc?export=view&id=1o4BXjOiqRTUQUdOq4FpMqq50NHoBSmAq" ,
                "https://drive.google.com/uc?export=view&id=1VDnvo2qkc80APQ-VALUaFRTLUVaEpQ3v" ,
                "https://drive.google.com/uc?export=view&id=1YPPqek7bC_Fp6_6WBrVuxaF5t4MbkSJp" ,
                "https://drive.google.com/uc?export=view&id=11MBBvxzAs8Cp5t6BeDTEeZBz0KzTHeBj" ,
                "https://drive.google.com/uc?export=view&id=1vZ0yoomfttLCWeqkaSBUI6KWnvn0uzMG" , 
                "https://drive.google.com/uc?export=view&id=1ipRtPRHSGI3m84B6mO_OCh1BdRbfOGuT" ,
        
                 
                
                "https://drive.google.com/uc?export=view&id=1yeayFr0CkKJSIzqjb-4_eRMMpPWUEmUH" ,
                "https://drive.google.com/uc?export=view&id=1x5D6xxmgz7lfxdwNWAJs8_4eHlMkJr-b"

                ]
                
            },
            "Word Combinations": {
                "audio": "https://drive.google.com/uc?id=1mMmicEMEbqS93HNcAwu6ZZzVwZd45Ecw&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=10KHP7RZoiP9Mq0uJGQD2ZGeyiNjWUYO8" ,
                "https://drive.google.com/uc?export=view&id=1LrlGrRcsQyFQGs4ZuYCKjVpJH_wCmu9Q"

                ]
            },
            "Quizlet": {
                "text_doc": """Quizlet:  
                \n\n Quizlet: Unit 6 Essential Vocabulary (https://quizlet.com/ru/893282041/ar-3-unit-6-essential-vocabulary-flash-cards/?funnelUUID=be860b53-c3cf-4e77-9036-617554c814b7)
                \n\n Quizlet: Unit 6 Topical vocabulary (https://quizlet.com/ru/896622341/ar3-unit-6-feelings-topixal-vocabulary-flash-cards/?funnelUUID=31da743c-bd03-44ef-be30-04fa5407c485)
                \n\n Quizlet: Unit 6 text (https://quizlet.com/ru/785487366/unit-6-text-flash-cards/?funnelUUID=80954aed-7df5-4761-bd2e-d60027d92c42)"""
                }
        },
        "Unit 7": {
            "Conversation and discussion": {
                "audio": "https://drive.google.com/uc?id=1Oph98EY4psJicalIcTVCyciQzBOjcLGP&export=download", 
                "image": [
                "https://drive.google.com/uc?export=view&id=1BIGmZoVDWMKR6XznDCXhLgm-O_F42wgF",
                "https://drive.google.com/uc?export=view&id=1CrfPUby9ZkopGADJQeB2DO6vZr98Qcu3",
                "https://drive.google.com/uc?export=view&id=1pReNVYLHAw4brei4NgCqvnvm7ojhlld0"
                ]
            },
            "Essential Vocabulary 1": {
                "audio": "https://drive.google.com/uc?id=1-3G4chtJtpGgUxs_A3m5QBLdR5ycS566&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=1gjOr-2NIMeOrF3Oq9EXdyhQdB7h1AdBs",
                "https://drive.google.com/uc?export=view&id=1d6I4AAFySQThxkiS2cxYfuKmC7TeUu-S",
                "https://drive.google.com/uc?export=view&id=1LEUMM6qfldG2hQaSKHZpN-JoE8lyezzS",
                "https://drive.google.com/uc?export=view&id=1lTdVz9l5kOI8gmi6PX0aFD7HCgpkTM_y",
                "https://drive.google.com/uc?export=view&id=1IAg0Qu18xwdDzU7ZlbUVPWB8pmvptLaE",
                "https://drive.google.com/uc?export=view&id=1b0fVc6Ca2AlYGC1BFsE-0fL8svhpwQ03",
                "https://drive.google.com/uc?export=view&id=17YHC7YSLKeTDi87BykOjYjSGR_FyvqFi",
                "https://drive.google.com/uc?export=view&id=1wLNhw9lnuknTb-fZKEMaXoFQX9rwYdLq",
                "https://drive.google.com/uc?export=view&id=1oTi5qGMF-G_qBg9V8qI8tiTBajOYiM2T",
                ]
            },
            "Essential Vocabulary 2": {
                "audio": "https://drive.google.com/uc?id=16pnSyV1J8j0ZENxix5ccvSHdOI5j_SjQ&export=download", 
                "image": [
                "https://drive.google.com/uc?export=view&id=1gjOr-2NIMeOrF3Oq9EXdyhQdB7h1AdBs",
                "https://drive.google.com/uc?export=view&id=1ZXYsUUxHzBDEi4wz_ttg8aSqK2s1Gy7c",
                "https://drive.google.com/uc?export=view&id=1fc2LaMMwIFr7ntdxRZGYwf7LvLlEPVbe",
                "https://drive.google.com/uc?export=view&id=1G5BQEIprp-fp3QXtvFzbEcJbacvyrf7_",
                "https://drive.google.com/uc?export=view&id=19U7vDVYlag1yBtoJwlk74ASN-SojreDl",
                "https://drive.google.com/uc?export=view&id=13BVs9Xhvf3VEHZiHKTDP8mh9fDXJ6qzk",
                "https://drive.google.com/uc?export=view&id=1BMPV3DW3q0BEkZo9qTxmEY4ON7_P9_6F"
                ]
            },
            "Speech Patterns": {
                "audio": "https://drive.google.com/uc?id=1hRVYckikjFc_OJG4XpMwnhQ_IERXUkN3&export=download", 
                "image": [
                "https://drive.google.com/uc?export=view&id=1fpZ2j8H-VJMRYIWgQXJSQKUl1sQBEb-c",
                "https://drive.google.com/uc?export=view&id=1peVF2PsaJXVouVbXAvGupQWJ51scYw0E",
                "https://drive.google.com/uc?export=view&id=1pspYl70TOelmoSbzpe_fQmy2LXgMXDL2",
                "https://drive.google.com/uc?export=view&id=12hVDmP96LbSrSFnayiM5WbyOynaNYkpM",
                "https://drive.google.com/uc?export=view&id=144Pnv2Lwsl6jM8Llo2Nenm1d7vMvdLiB",
                "https://drive.google.com/uc?export=view&id=1iw854qReJBtbCM2N__n0ZOtsG4cjAN-z",
                "https://drive.google.com/uc?export=view&id=1DlGk3EdGdZu8J-0vaxvUuvxhyENi7vu-",
                "https://drive.google.com/uc?export=view&id=1YT7xq-A8q0UGG8LDU3C7U4MyZCQVwd4M",
                "https://drive.google.com/uc?export=view&id=1gG3p1wNoYLZ9UCtb83ujze2sjjF02Xhy"
                ]
            },
            "Word Combinations": {
                "audio": "https://drive.google.com/uc?id=1K3SUhqDnGw4ulV-IAPIVzSdz_VPLHm18&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1MUUipuxyn6CvHz1DxPYI1q1chZYiEfqU",
                "https://drive.google.com/uc?export=view&id=1PwqE_FcXqvIDB1FkW4AWHxF0bpIUNef4"
                ]
                
                
            },
            "Quizlet": {
                "text_doc": """Quizlet:  
                \n\n Quizlet: Unit7 Essential vocabulary (https://quizlet.com/ru/903651935/ar3-unit7-essential-vocab-flash-cards/?funnelUUID=a71b49fe-a1f2-4cd3-859f-ab870a2f93a5)
                \n\n Quizlet: Unit 7 Topical Vocabulary Positive qualities (https://quizlet.com/ru/907784798/ar-3-unit-7-topical-vocab-positive-qualities-flash-cards/?funnelUUID=47bfd386-76a1-47a6-8a92-0990dfd4c30c)
                \n\n Quizlet: Unit 7 Topical Vocabulary Negative Qualities (https://quizlet.com/ru/907785229/ar-3-unit-7-negative-qualities-flash-cards/?funnelUUID=52fc8a24-b909-442b-89b8-81288969cfe0)
                \n\n Quizlet: Unit 7 Text  Essential Voccabulary (https://quizlet.com/ru/793345464/text-7-essential-vocabulary-flash-cards/?funnelUUID=1c57b63c-0f3f-4278-aa8a-6a18cbd55f83)"""
                }
                
                

        },
        "Unit 8": {
            "Conversation and discussion": {
                "audio": "https://drive.google.com/uc?id=1Ol9VLRE6QA0Ark3cfR8jS7kwmL8t2_nh&export=download", 
                "image": [
                "https://drive.google.com/uc?export=view&id=1iYxqJi8EC6Hqj8tbrtYaDW3KqCfPxjUc",
                "https://drive.google.com/uc?export=view&id=1nST6g30cZihnyTHuZryDjEvHgaeR8eqC",
                "https://drive.google.com/uc?export=view&id=1roET2cdFxo0OapnkOZ5ta2b6tl1u7awj",
                "https://drive.google.com/uc?export=view&id=1FShwdca3JYeLZ1aZw6c-1mWlFzAOPXXz",
                "https://drive.google.com/uc?export=view&id=1IuZBt4PgJ0-T_Tqj1PGNwMjg5KdozPnX"
                ]
            },
            "Essential Vocabulary 1": {
                "audio": "https://drive.google.com/uc?id=1JFY_24F44_MBOmR0FCdNDsTl7Mm4FBWb&export=download",
                "image": [
                "https://drive.google.com/uc?export=view&id=18DrdFHuL4Ty7H-5FeIylXkCr_CJShlQu",
                "https://drive.google.com/uc?export=view&id=10oXtv8tVMkYBoBML-XWM436gVXtTpvHm",
                "https://drive.google.com/uc?export=view&id=1V8Inl9ucghqzBIrxX-JrPnbXcKD50QIG",
                "https://drive.google.com/uc?export=view&id=16flbOGAuJ8znI3SqhH8zm0UhtyaksQLi",
                "https://drive.google.com/uc?export=view&id=1pwHWK-wk7qQ2kV-wazroP2fOcpIbvGc8",
                "https://drive.google.com/uc?export=view&id=1QUGb6I21gg-mBLjZvadqgAgZ3wZwSyA4",
                "https://drive.google.com/uc?export=view&id=1JqCraL-flTwT9B4HJGXN2c2yB8ypwOMb",
                "https://drive.google.com/uc?export=view&id=1NIwQ86it5MmoERjcf2g5bYr1gHk0ohk2",
                "https://drive.google.com/uc?export=view&id=1g2IpT9Ub9qfWwdBbnmKZmeOfPgZQIRmv"
                ]
            },
            "Essential Vocabulary 2": {
                "audio": "https://drive.google.com/uc?id=1MltaI7UC0kodmGUzwRZv2z_ip3tectVv&export=download", 
                "image": [
                "https://drive.google.com/uc?export=view&id=18DrdFHuL4Ty7H-5FeIylXkCr_CJShlQu" ,
                "https://drive.google.com/uc?export=view&id=1kCVTQIxtDxY_ZnxG6HS-22OVR7ciEz46",
                "https://drive.google.com/uc?export=view&id=1dD_El8aW-ahuj8wdvF0MaW-7uCfSut9i",
                "https://drive.google.com/uc?export=view&id=1sZ1EfvflqMi3ExlmVotv6yWtbSDIIAIa",
                "https://drive.google.com/uc?export=view&id=13IEg37Dt5ShhpSOpD1iOMYyYFsKlZ3zk",
                "https://drive.google.com/uc?export=view&id=1tYMZotx9PFdPj2IoeI2WbMrLm5Cill-O"
                ]   
            },
            "Speech Patterns": {
                "audio": "https://drive.google.com/uc?id=19RMbVAKJVfbJaUKNcXUFQBbtQgE1nufs&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1ZFcisunQqGBxnrnQplzKtu3KHOezd2K-",
                "https://drive.google.com/uc?export=view&id=1tjMFATvVYdasP0-1HIasLzoV0zUg3neI",
                "https://drive.google.com/uc?export=view&id=1DtxAfvZ5IKYRz2lMgbJh2ok7C66eeHM9",
                "https://drive.google.com/uc?export=view&id=1UP2d8vULYw5cm0d6o0pavjTuXcfelZUl",
                "https://drive.google.com/uc?export=view&id=1DgRzop4jaOUGPFoRj4mNkz4LfSjfDv8w",
                "https://drive.google.com/uc?export=view&id=1CUey0CL3-U9YIuYQa157JUv4Hws9CJxc",
                "https://drive.google.com/uc?export=view&id=1wMA1__R8Mn0SooEwZvdRKWqyhgl2iswj"
                ]
            },
            "Word Combinations": {
                "audio": "https://drive.google.com/uc?id=1swXtpDqZej82MuuslGVkLQ809vuaNP5i&export=download" ,
                "image": [
                "https://drive.google.com/uc?export=view&id=1rHKI8DTntrUvAqgcHo_aO_rsXId_oCZ7" ,
                "https://drive.google.com/uc?export=view&id=1l1JPOgHJuOQXYbJML8WBnKWJNHx7RPsi"
                ]

            },
            "Quizlet": {
                "text_doc": """Quizlet:  
                \n\n Quizlet: Unit 8 Essential Vocabulary (https://quizlet.com/ru/804021638/unit-8-essential-vocabulary-flash-cards/?funnelUUID=539a7242-3e77-4f1c-a9f1-2ad4e6e7bd55)"""
                }
        }
    }
}



def start(update: Update, context: CallbackContext) -> None: #функция старт
    keyboard = [[InlineKeyboardButton(course, callback_data=course)] for course in AUDIO_FILES.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Привет! Устал читать учебник Аракина? Тогда слушай лексику и запоминай:) В телеграм-боте собраны аудиофайлы для разделов Conversation and discussion, Essential Vocabulary 1, Essential Vocabulary 2, Speech Patterns и Word Combinations, а также ссылки на Quizlet. Good luck;)", reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    data = query.data

    if data in AUDIO_FILES:
        keyboard = [[InlineKeyboardButton(unit, callback_data=f"{data}|{unit}")] for unit in AUDIO_FILES[data].keys()]
        query.message.reply_text("Выберите Unit:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif "|" in data:
        parts = data.split("|")
        if len(parts) == 2:
            course, unit = parts
            keyboard = [[InlineKeyboardButton(category, callback_data=f"{course}|{unit}|{category}")] for category in AUDIO_FILES[course][unit].keys()]
            query.message.reply_text("Выберите категорию:", reply_markup=InlineKeyboardMarkup(keyboard))
        elif len(parts) == 3:
            course, unit, category = parts
            chat_id = query.message.chat_id
            file_data = AUDIO_FILES.get(course, {}).get(unit, {}).get(category)

            if file_data:
                audio_url = file_data.get("audio")
                text_doc = file_data.get("text_doc")
                image_urls = file_data.get("image", [])  # Получаем список изображений

                # Отправка аудио
                if audio_url:
                    query.message.reply_audio(audio_url)

                # Отправка текста
                if text_doc:
                    context.bot.send_message(chat_id=chat_id, text=text_doc)

                # Отправка до 10 изображений одним сообщением
                if isinstance(image_urls, list) and image_urls:
                    media_group = [InputMediaPhoto(media=url) for url in image_urls[:10]]
                    context.bot.send_media_group(chat_id=chat_id, media=media_group)

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton(course, callback_data=course)] for course in AUDIO_FILES.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Ссылка на картинку
    image_url = "https://drive.google.com/uc?export=view&id=10pTukDmB4b_omAj7S0q4lgGUvz9hPGXH"  # Здесь укажите вашу ссылку на картинку

    update.message.reply_photo(
        photo=image_url,
        caption=(
        "·Цифровой учебник с лексикой из В.Д. Аракина Практический курс английского (3 курс).\n\n"
        "✧Аудиофайлы для разделов:\n"
        "∘Conversation and discussion\n"
        "∘Essential Vocabulary 1\n"
        "∘Essential Vocabulary 2\n"
        "∘Speech Patterns\n"
        "∘Word Combinations\n\n"
        "∘Ссылки на Quizlet\n\n"
        "∘Дизайнерские картинки для лучшего запоминания лексики\n\n"
        "✧Good luck!"
        ),
        reply_markup=reply_markup 
        
    )

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
