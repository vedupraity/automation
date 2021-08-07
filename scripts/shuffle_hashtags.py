import random

tags = [
  # primary hashtags
  'ancientknowledge praacheengyaan sanatandharma bhagavadgita',
  # secondary hashtags
  'ancient knowledge education spirituality hinduism krishna lordkrishna harekrishna sanatandharma sanatani mahabharat ramayana vedas hindu wisdom india meditation yoga namaste bhagavadgitaquotes',
  # optional hashtags
  'instagram insta instalike instadaily instagood lifestyle lifelessons motivationalquotes motivation life book likeaboss likefollow quotes love bookstagram'
]

def shuffle_hashtags(tags):
    total_hashtag_limit = random.randrange(18,26)

    primary_hashtag_list = ['#' + _ for _ in tags[0].split()]
    primary_hashtag_limit = len(primary_hashtag_list)

    secondary_hashtag_list = ['#' + _ for _ in tags[1].split()]
    secondary_hashtag_limit = int((total_hashtag_limit - primary_hashtag_limit) * 0.60)

    optional_hashtag_list = ['#' + _ for _ in tags[2].split()]
    optional_hashtag_limit = total_hashtag_limit - (primary_hashtag_limit + secondary_hashtag_limit)

    selected_primary_hashtags = primary_hashtag_list[0:primary_hashtag_limit]

    random.shuffle(secondary_hashtag_list)
    selected_secondary_hashtags = secondary_hashtag_list[0:secondary_hashtag_limit]

    random.shuffle(optional_hashtag_list)
    selected_optional_hashtags = optional_hashtag_list[0:optional_hashtag_limit]

    return selected_primary_hashtags + selected_secondary_hashtags + selected_optional_hashtags

print(' '.join(shuffle_hashtags(tags)))
