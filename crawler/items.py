# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ForumItem(Item):
    url = Field()
    course_name = Field()


class SubForumItem(Item):
    name = Field()
    url = Field()


class ThreadItem(Item):
    url = Field()a#the thread url
    votes_cnt = Field()
    posts_cnt = Field()
    views_cnt = Field()
    tags = Field()

class PostItem(Item)
    """post in the thread"""
    url = Field() #the thread url
    votes_cnt = Field()
    text = Field()
    onwer = Field()
    time = Field()

class CommentItem(Item):
    """comment within the post"""
    url = Field() #the thread url
    votes_cnt = Field()
    text = Field()
    onwer = Field()
    time = Field()
