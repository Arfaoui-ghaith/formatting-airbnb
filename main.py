import os

import pandas as pd
import json

directories = [x[0] for x in os.walk("../milestone 1/")]

print(directories[1::])

df = pd.read_csv('../milestone 1/alabama/listings.csv',
                 usecols=["scrapedAt", "listingId", "title", "metaPrice.currencyCode", "metaPrice.symbol",
                          "metaPrice.floatValue", "image", "description", "category", "discount", "rating",
                          "reviewsCount", "seller.badge", "seller.avatar", "seller.features", "seller.tags",
                          "seller.name", "breadcrumbs", "location", "lat", "lng", "guests", "pets_allowed",
                          "description_items", "category_rating", "rules", "details", "highlights", "neighborhood",
                          "nearbyCities", "arrangement_details", "amenities", "images", "propertyType", "url"],
                 sep=';', encoding='utf-8')

data = df
for index, row in data.iterrows():
    dataRow = row.to_dict()

    listingId = None if pd.isna(dataRow['listingId']) or dataRow['listingId'] == 'undefined' else dataRow['listingId']
    title = None if pd.isna(dataRow['title']) or dataRow['title'] == 'undefined' else dataRow['title']
    meta_price_currency = None if pd.isna(dataRow['metaPrice.currencyCode']) or dataRow[
        'metaPrice.currencyCode'] == 'undefined' else dataRow['metaPrice.currencyCode']
    meta_price_symbol = None if pd.isna(dataRow['metaPrice.symbol']) or dataRow['metaPrice.symbol'] == 'undefined' else \
        dataRow['metaPrice.symbol']
    meta_price_value = None if pd.isna(dataRow['metaPrice.floatValue']) or dataRow[
        'metaPrice.floatValue'] == 'undefined' else dataRow['metaPrice.floatValue']
    image = None if pd.isna(dataRow['image']) or dataRow['image'] == 'undefined' else dataRow['image']
    description = None if pd.isna(dataRow['description']) or dataRow['description'] == 'undefined' else dataRow[
        'description']
    category = None if pd.isna(dataRow['category']) or dataRow['category'] == 'undefined' else dataRow['category']
    discount = None if pd.isna(dataRow['discount']) or dataRow['discount'] == 'undefined' else dataRow['discount']
    rating = None if pd.isna(dataRow['rating']) or dataRow['rating'] == 'undefined' else dataRow['rating']
    reviews_count = None if pd.isna(dataRow['reviewsCount']) or dataRow['reviewsCount'] == 'undefined' else dataRow[
        'reviewsCount']
    host_badge = None if pd.isna(dataRow['seller.badge']) or dataRow['seller.badge'] == 'undefined' else dataRow[
        'seller.badge']
    host_avatar = None if pd.isna(dataRow['seller.avatar']) or dataRow['seller.avatar'] == 'undefined' else dataRow[
        'seller.avatar']
    host_name = None if pd.isna(dataRow['seller.name']) or dataRow['seller.name'] == 'undefined' else dataRow[
        'seller.name']
    host_languages = None
    host_response_rate = None
    host_response_time = None
    host_reviews_count = None
    host_airbnb_supporter = False
    host_hasLicense = False
    host_license_number = None
    host_Identity_verified = False
    host_isExperienced = False
    breadcrumbs = None
    location = None
    description_items = None
    beds = None
    baths = None
    bedrooms = None
    if not (pd.isna(dataRow['seller.features']) or dataRow['seller.features'] == 'undefined'):
        for feature in json.loads(dataRow['seller.features']):
            if feature['title'] == 'Languages':
                host_languages = feature['subtitle']
            if feature['title'] == 'Response rate':
                host_response_rate = feature['subtitle']
            if feature['title'] == 'Response time':
                host_response_time = feature['subtitle']
            if feature['title'] == 'Registration number':
                host_hasLicense = True
                host_license_number = feature['subtitle']

    if not (pd.isna(dataRow['seller.tags']) or dataRow['seller.tags'] == 'undefined'):
        for tag in json.loads(dataRow['seller.tags']):
            if tag['title'].find('Reviews') > -1:
                host_reviews_count = tag['title'].split()[0]
            if tag['title'].find('Identity verified') > -1:
                host_Identity_verified = True
            if tag['title'].find('supporter') > -1:
                host_airbnb_supporter = True

    if not (pd.isna(dataRow['breadcrumbs']) or dataRow['breadcrumbs'] == 'undefined'):
        breadcrumbs = [(b['title'] if 'title' in b.keys() else '') for b in
                       json.loads(dataRow['breadcrumbs'])]

    if len(breadcrumbs) > 0: location = breadcrumbs[-1] if pd.isna(dataRow['location']) or dataRow[
        'location'] == 'undefined' else dataRow['location']
    lat = None if pd.isna(dataRow['lat']) or dataRow['lat'] == 'undefined' else dataRow['lat']
    lng = None if pd.isna(dataRow['lng']) or dataRow['lng'] == 'undefined' else dataRow['lng']

    guests = None if pd.isna(dataRow['guests']) or dataRow['guests'] == 'undefined' else dataRow['guests']
    pets_allowed = None if pd.isna(dataRow['pets_allowed']) or dataRow['pets_allowed'] == 'undefined' else dataRow[
        'pets_allowed']
    category = None if pd.isna(dataRow['category']) or dataRow['category'] == 'undefined' else dataRow['category']

    if not (pd.isna(dataRow['description_items']) or dataRow['description_items'] == 'undefined'):
        description_items = [item['title'] for item in json.loads(dataRow['description_items'])]
        for item in json.loads(dataRow['description_items']):
            if item['title'].find('bed') > -1:
                beds = item['title'].split()[0]
            if item['title'].find('bath') > -1:
                baths = item['title'].split()[0]

    AccuracyRating = None
    CheckinRating = None
    CleanlinessRating = None
    CommunicationRating = None
    LocationRating = None
    ValueRating = None

    if not (pd.isna(dataRow['category_rating']) or dataRow['category_rating'] == 'undefined'):
        for rating in json.loads(dataRow['category_rating']):
            if rating['name'].find('Accuracy') > -1:
                AccuracyRating = rating['value']
            if rating['name'].find('Checkin') > -1:
                CheckinRating = rating['value']
            if rating['name'].find('Cleanliness') > -1:
                CleanlinessRating = rating['value']
            if rating['name'].find('Communication') > -1:
                CommunicationRating = rating['value']
            if rating['name'].find('Location') > -1:
                LocationRating = rating['value']
            if rating['name'].find('Value') > -1:
                ValueRating = rating['value']

    rules = None
    if not (pd.isna(dataRow['rules']) or dataRow['rules'] == 'undefined'):
        rules = [item['title'] for item in json.loads(dataRow['rules'])]

    details = None
    if not (pd.isna(dataRow['details']) or dataRow['details'] == 'undefined'):
        details = [item['title'] for item in json.loads(dataRow['details'])]
        for detail in json.loads(dataRow['details']):
            if detail['title'].find('bedroom') > -1:
                bedrooms = detail['title'].split()[0]

    highlights = None
    wifi = False
    workspace = False
    if not (pd.isna(dataRow['highlights']) or dataRow['highlights'] == 'undefined'):
        highlights = []
        for h in json.loads(dataRow['highlights']):
            subtitle = ' : ' + h['subtitle'] if 'subtitle' in h.keys() and h['subtitle'] is not None else ''
            highlight = h['title'] + subtitle
            highlights.append(highlight)
            if highlight.find('wifi') > -1:
                wifi = True
            if highlight.find('workspace') > -1:
                workspace = True
            if highlight.find('Experienced host') > -1:
                host_isExperienced = True

    neighborhood = None
    if not (pd.isna(dataRow['neighborhood']) or dataRow['neighborhood'] == 'undefined'):
        neighborhood = (''.join([item['searchText'] for item in json.loads(dataRow['neighborhood'])])).strip()

    nearbyCities = None
    if not (pd.isna(dataRow['nearbyCities']) or dataRow['nearbyCities'] == 'undefined'):
        nearbyCities = [item['title'] for item in json.loads(dataRow['nearbyCities'])]

    arrangement_details = None
    if not (pd.isna(dataRow['arrangement_details']) or dataRow['arrangement_details'] == 'undefined'):
        arrangement_details = list(set([item['subtitle'] for item in json.loads(dataRow['arrangement_details'])]))

    amenities = None
    if not (pd.isna(dataRow['amenities']) or dataRow['amenities'] == 'undefined'):
        amenities = dataRow['amenities']

    images = None
    if not (pd.isna(dataRow['images']) or dataRow['images'] == 'undefined'):
        images = arrangement_details = [item['baseUrl'] for item in json.loads(dataRow['images'])]

    propertyType = None if pd.isna(dataRow['propertyType']) or dataRow['propertyType'] == 'undefined' else dataRow['propertyType']
    url = None if pd.isna(dataRow['url']) or dataRow['url'] == 'undefined' else dataRow['url']


