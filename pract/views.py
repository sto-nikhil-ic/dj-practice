from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string # y0  khasei   use hudeina yesko sato rnder using shorcut ko lag

# Create you views here.
month_data = {
    "january": "January marks the heart of winter in the Northern Hemisphere, with cold temperatures and often snow in many regions. It begins the new calendar year with celebrations on January 1st. Notable events include International Education Day on the 24th and Maghe Sankranti in Nepal, which celebrates the end of winter solstice and the beginning of longer days.",
    
    "february": "February remains a chilly winter month but hints at the coming spring. It’s the shortest month of the year and includes Valentine’s Day on the 14th, International Mother Language Day on the 21st, and often features Maha Shivaratri, a significant Hindu festival celebrated with devotion and fasting.",
    
    "march": "March brings the arrival of spring, with blooming flowers and longer days. The month includes International Women’s Day on March 8th and World Water Day on March 22nd. In South Asia, Holi—the festival of colors—is celebrated with joy and vibrant festivities.",
    
    "april": "April is a beautiful spring month known for pleasant weather and blooming nature. It features Earth Day on April 22nd and, in Nepal, marks the beginning of the Nepali New Year in mid-April. Religious events such as Ram Navami and Easter (which may fall in April) are also observed.",
    
    "may": "May is a late spring month where the weather turns warmer, especially in South Asia where it starts to get humid. Important events include International Workers’ Day on May 1st, Buddha Jayanti (birth of Lord Buddha), and Mother's Day in Nepal. It is also a time when schools may begin summer breaks.",
    
    "june": "June marks the beginning of summer and includes the summer solstice—the longest day of the year. It features World Environment Day on June 5th and Father's Day (celebrated in many countries on the third Sunday). In Nepal, June is known for Ropain Diwas, the traditional rice planting festival celebrated by farmers.",
    
    "july": "July is a hot and humid summer month and part of the monsoon season in South Asia. It includes U.S. Independence Day on July 4th, World Population Day on July 11th, and Guru Purnima—a day to honor teachers and mentors.",
    
    "august": "August is typically the peak of the monsoon season in Nepal and India. The month is rich in cultural celebrations, including Raksha Bandhan (symbolizing sibling bonds), Krishna Janmashtami (celebrating Lord Krishna’s birth), and Gaijatra in Nepal, which honors the dead with processions and humor.",
    
    "september": "September signals the end of the monsoon and the start of autumn. The weather becomes more pleasant with clearer skies. Important observances include Nepal’s Constitution Day on September 20th, International Day of Peace on the 21st, and Teacher’s Day in Nepal (on Guru Purnima, if not in July).",
    
    "october": "October is a vibrant and festive autumn month. In Nepal, the major festival Dashain is celebrated with family gatherings, blessings, and animal sacrifices. The weather is cool and dry. Globally, it includes World Mental Health Day on October 10th and Halloween on October 31st.",
    
    "november": "November brings late autumn with cooler temperatures and clearer skies. It features the festival of Tihar (or Deepawali) in Nepal, celebrated with lights, songs, and honoring of animals like crows, dogs, and cows. Other global events include World Children’s Day on November 20th and Thanksgiving in the United States.",
    
    "december": "December is a chilly winter month, often associated with snow and festive cheer. Christmas is celebrated globally on December 25th, and the month ends with New Year’s Eve on December 31st. International Human Rights Day is observed on December 10th, promoting awareness and activism."
}

def empty(request):
    list_month=""
    dicmonth=list(month_data.keys())
    return render(request, "pract/index.html",{
        "months":dicmonth
    })
def number(request,month):
    
    if month>12:
        return HttpResponse("errror month")
    
    month=month-1 #LSIT 0 DEKHI SURU HUNCHA
    dicmonth=list(month_data.keys())
    forward_month=dicmonth[month]
    redirect_path =reverse("month-",args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def months(request, month):
    try:
        text=month_data[month]
        # html=render_to_string("pract/pract.html")
        # return HttpResponse(html) //yesko sato diret render use gard hucnha
        return render(request,"pract/pract.html",{
            "text":text,
            "monthname":month
        })
    except:
        
         return HttpResponseNotFound("not found")
    
    