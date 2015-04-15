
#building a Shopify App -> PHP
    https://github.com/phpish/shopify_private_app-skeleton



#AUTHENTICATION
request = requests.Session(auth=(settings.SHOPIFY_API_KEY, settings.SHOPIFY_API_PASSWORD))
print json.loads(request.get('http://myshop.myshopify.com/admin/assets.json').content)



#CREATE A PRODUCT:

payload = '''{
      "product": {
        "body_html": "<strong>Good snowboard!</strong>",
        "product_type": "Snowboard",
        "title": "Burton Custom Freestlye 151",
        "variants": [
          {
            "price": "10.00",
            "option1": "First"
          },
          {
            "price": "20.00",
            "option1": "Second"
          }
        ],
        "vendor": "Burton"
      }
    }'''
 
response = request.post('http://myshop.myshopify.com/admin/products',
    data=payload,
    headers={''Content-Type': 'application/json', # this is the important part.}
print response.status_code, response.content

#MODIFY AN EXISTING PRODUCT

payload = '''{
      "product": {
        "published": false,
        "id": 632910392
      }
    }'''
response = request.put('http://myshop.myshopify.com', data=payload, headers={'Content-Type': 'application/json'})


------------------------------------------------------
public string GetCustomers()
{
    const string url = "https://your-store.myshopify.com/admin/customers.json";
    
    var req = (HttpWebRequest)WebRequest.Create(url);
    req.Method = "GET";
    req.ContentType = "application/json";
    req.Credentials = GetCredential(url);
    req.PreAuthenticate = true;

using (var resp = (HttpWebResponse)req.GetResponse())
{
        if (resp.StatusCode != HttpStatusCode.OK)
        {
            string message = String.Format("Call failed. Received HTTP {0}", resp.StatusCode);
            throw new ApplicationException(message);
        }
        var sr = new StreamReader(resp.GetResponseStream());
        return sr.ReadToEnd();
    }
}

private static CredentialCache GetCredential(string url)
{
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3;
    var credentialCache = new CredentialCache();
    credentialCache.Add(new Uri(url), "Basic", new NetworkCredential("your-api-key", "your-password"));
    return credentialCache;
} 


--------------------------------------------------------


#This is a really cool 
 yuchant / gist:312d42568192a2bf3acc SECRET
Created on Jan 30, 2014

import re
from flask import render_template, request
 
from . import module
 
from grovemade import cache
from grovemade_admin.shop.shopify_sync import shopify
 
from BeautifulSoup import BeautifulSoup
 
 
GROVE_BLOG_ID = 2839566
 
 
@cache.memoize(timeout=60*30)
def get_all_shopify_posts():
    '''
    Get all blog posts from Shopify API.
    - Get posts from shopify until exhausted. This can take many seconds. Cache.
    - Post process posts to be more consistent
        - extract first image
        - remove tags
    '''
 
    def strip_tags(text):
        return re.sub('<[^<]+?>', '', text)
 
    def get_first_image_src(html):
        tree = BeautifulSoup(html)
        img = tree.find('img')
        return img.get('src') if img else None
 
    def get_shopify_posts(since_id=None):
 
        return list(shopify.Article(prefix_options={'GROVE_BLOG_ID': GROVE_BLOG_ID}).find(
            limit=250,
            published_status='published',
            since_id=since_id,
        ))
 
    posts = get_shopify_posts()
    blog_posts = posts
 
    # keep calling shopify until results exhausted
    while len(posts) == 250:
        posts = get_shopify_posts(since_id=posts[-1].id)
        blog_posts.extend(posts)
 
    blog_posts.reverse()
 
    # update shopify posts with our own cleaned data
    for post in blog_posts:
        post.cleaned_body = strip_tags(post.body_html)
        post.first_image = get_first_image_src(post.body_html)
    return blog_posts
 
 
def get_page(page, paginate_by=25):
    '''
    Paginator
    '''
    posts = get_all_shopify_posts()
    posts_by_slice = [posts[i:i+paginate_by] for i in range(0, len(posts), paginate_by)]
    return posts_by_slice[page]
 
 
@module.route('/')
@module.route('/<int:page>/')
def index(page=0):
    ctx = {
        'blog_posts': get_page(page, paginate_by=30),
    }
    return render_template('blog/index.html', **ctx)
 
 
@module.route('/<int:id>/<title>/')
@cache.cached(timeout=60)
def post_detail(id, title):
    ctx = {
        'blog_post': shopify.Article(prefix_options={'GROVE_BLOG_ID': GROVE_BLOG_ID}).find(id)
    }
    return render_template('blog/detail.html', **ctx)

Write Preview Parsed as Markdown  Edit in fullscreen

Comment
Status API Blog About © 2015 GitHub, Inc. Terms Privacy Security Contact 