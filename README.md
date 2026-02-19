There should be ten different Channel objects inside of the chats list. To access it you can check the code inside of service_discovery.py.
Make sure to be aware of the information that is being scraped from each of the channels.

```python
chats= [      
    Channel(
            id=1424801960,
            title='ក្រសួងកសិកម្ម រុក្ខាប្រមាញ់ និងនេសាទ',
            photo=ChatPhoto(
                    photo_id=6332552828819716309,
                    dc_id=5,
                    has_video=False,
                    stripped_thumb=b'\x01\x08\x08\xb2\x1a\x7f;\x1f>wzqE\x14P\x16\xb1'
            ),
            date=datetime.datetime(2020, 11, 7, 5, 26, 45, tzinfo=datetime.timezone.utc),
            creator=False,
            left=True,
            broadcast=True,
            verified=False,
            megagroup=False,
            restricted=False,
            signatures=False,
            min=False,
            scam=False,
            has_link=False,
            has_geo=False,
            slowmode_enabled=False,
            call_active=False,
            call_not_empty=False,
            fake=False,
            gigagroup=False,
            noforwards=False,
            join_to_send=False,
            join_request=False,
            forum=False,
            stories_hidden=False,
            stories_hidden_min=True,
            stories_unavailable=True,
            signature_profiles=False,
            autotranslation=False,
            broadcast_messages_allowed=False,
            monoforum=False,
            forum_tabs=False,
            access_hash=-2988788926924533429,
            username='maff_gov_kh',
            restriction_reason=[
            ],
            admin_rights=None,
            banned_rights=None,
            default_banned_rights=None,
            participants_count=8986,
            usernames=[
            ],
            stories_max_id=None,
            color=None,
            profile_color=None,
            emoji_status=None,
            level=None,
            subscription_until_date=None,
            bot_verification_icon=None,
            send_paid_messages_stars=None,
            linked_monoforum_id=None
        ),
]
```