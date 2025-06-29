from django.shortcuts import render
from datetime import date
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseNotFound
from django.template.loader import render_to_string

all_posts=[
    {
        "slug":"My-DSA-Journey",
        "image":"hello.jpg",
        "author":"Rohit",
        "date":date(2025,6,27),
        "title":"My DSA Journey",
        "excerpt":"I am a ug student at IIT Jammu, I like videography and problem solving. Currently in my 3rd year in my BTech Cse Program",
        "content":"""
         In the vast canvas of possibilities, every moment holds a new beginning. The wind doesn’t ask for direction, and yet it moves with purpose — perhaps we should too. Whether it’s a quiet morning or a stormy night, the world continues to spin its stories, waiting for someone to listen, to write, or to live them fully.
         
         In the vast canvas of possibilities, every moment holds a new beginning. The wind doesn’t ask for direction, and yet it moves with purpose — perhaps we should too. Whether it’s a quiet morning or a stormy night, the world continues to spin its stories, waiting for someone to listen, to write, or to live them fully.
         
         In the vast canvas of possibilities, every moment holds a new beginning. The wind doesn’t ask for direction, and yet it moves with purpose — perhaps we should too. Whether it’s a quiet morning or a stormy night, the world continues to spin its stories, waiting for someone to listen, to write, or to live them fully.
        """
    },
    {
        "slug": "Cracking-My-First-Interview",
        "image": "interview.jpg",
        "author": "Rohit",
        "date": date(2025, 5, 20),
        "title": "Cracking My First Interview",
        "excerpt": "A journey through the ups and downs of preparing for my very first technical interview and what I learned along the way.",
        "content": """
        Nervous hands, rehearsed answers, and sleepless nights — my first interview wasn’t just a test of knowledge but of patience and self-belief. I revised every DSA concept, practiced mock interviews, and yet, nothing could fully prepare me for the real thing.

        But when the questions came, I surprised myself — not by knowing everything, but by staying calm and reasoning through what I didn’t know. That was the real win. 

        This experience taught me that interviews aren’t just checkpoints — they’re mirrors. And sometimes, what they reflect can be more valuable than a job offer.
        """
    },
    {
        "slug": "Why-I-Fell-in-Love-with-Python",
        "image": "python.png",
        "author": "Rohit",
        "date": date(2025, 3, 12),
        "title": "Why I Fell in Love with Python",
        "excerpt": "From basic scripts to building real-world ML models, Python has been my constant companion in this coding adventure.",
        "content": """
        I wrote my first line of Python to automate a boring file renaming task. What started as a lazy shortcut became the gateway to a whole new world of problem-solving.

        Python’s simplicity hides a powerful engine. It let me focus on *what* I wanted to build, not how to fight the syntax. From scraping websites to creating machine learning models, every project I touched became a little more fun.

        I fell in love with coding again — not for grades or resume points, but for the joy of creating. And Python was the language that made it possible.
        """
    }   
]
def get_date(post):
    return post['date']

def index(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"home/index.html",{
        "posts":latest_posts
    })

def posts(request):
    return render(request,"home/all-posts.html",{
        "all_posts":all_posts
    })

def posts_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "home/post-detail.html", {
      "post": identified_post
    })
