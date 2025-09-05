---
title: MGR API Documentation
language_tabs:
  - json: JSON
  - shell: cURL
---

## REST API for the MGR platform.

### Authentication

Authentication is done via an **Authorization** Header. Successfully signing in as
a user, business staff, app, etc. will return an api token. This token can be
sent with all subsequent requests via the **Authorization: Bearer {your-api-token}** header.

# Business Accounts

A Business Account is a gym or studio with one or many locations.
It is the top-level entity for pretty much everything.
By accessing the API from a specific domain, you are generally mapping to a specific business account.
Generally, this will be called once when the app loads. For example, if the user visits http://www.joes-gym.com
and the web app makes a fetch call to **/api/business_account/current**, the API will look at the
ORIGIN header, and return the data associated with the Joes Gym Business Account.


## Get Current

Ask the API for what my current Business Account is based on host origin.

### Request

#### Endpoint

```plaintext
GET /api/business_accounts/current
Origin: http://swaniawski.name
Host: example.org
Cookie: 
```

`GET /api/business_accounts/current`

#### Parameters


None known.


### Response

```plaintext
Content-Type: application/json; charset=utf-8
Access-Control-Allow-Origin: http://swaniawski.name
Access-Control-Allow-Methods: GET,PUT,POST,DELETE
Access-Control-Allow-Headers: Authorization,Content-Type
Vary: Origin
ETag: W/&quot;2c2f832a2b606eb3021f53dfc3a829cc&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: c98fa62b-99ea-4da0-8686-05e4affb3b49
X-Runtime: 0.149406
Content-Length: 1654
200 OK
```


```json
{
  "business_account": {
    "id": "b7b5b8bc-ffde-4465-b437-7ccef28d3c82",
    "name": "Sanford Group",
    "slug": "sanford-group",
    "business_type": "fitness_studio",
    "account_type": null,
    "requires_waiver": true,
    "waiver_text": null,
    "default_time_zone": "America/Los_Angeles",
    "schedule_release_type": "monthly",
    "schedule_release_day": 20,
    "schedule_release_time": "12:00am",
    "on_classpass": false,
    "contact_email": null,
    "locations": [
      {
        "id": "f063bd70-041f-466e-8264-436c3ead9ffd",
        "name": "O'Conner, Homenick and Carter",
        "slug": "o-conner-homenick-and-carter",
        "address1": null,
        "address2": null,
        "city": null,
        "state": null,
        "zip_code": null,
        "contact_email": null,
        "phone": null,
        "latitude": null,
        "longitude": null,
        "time_zone": "America/Los_Angeles",
        "reservations_open_until": "2019-06-30T23:59:00.000-07:00",
        "next_schedule_release_at": "2019-06-20T00:00:00.000-07:00",
        "allow_guest_only_reservations": true,
        "show_waitlist_capacity": true,
        "default_schedule_display_period": null,
        "late_cancel_policy": null,
        "waitlist_policy": null,
        "no_show_fee": "0.0",
        "late_cancel_fee": "0.0",
        "location_tax_categories": [

        ]
      },
      {
        "id": "3da201a1-0864-4af1-a41a-be430d35bd13",
        "name": "Shields-Deckow",
        "slug": "shields-deckow",
        "address1": null,
        "address2": null,
        "city": null,
        "state": null,
        "zip_code": null,
        "contact_email": null,
        "phone": null,
        "latitude": null,
        "longitude": null,
        "time_zone": "America/Los_Angeles",
        "reservations_open_until": "2019-06-30T23:59:00.000-07:00",
        "next_schedule_release_at": "2019-06-20T00:00:00.000-07:00",
        "allow_guest_only_reservations": true,
        "show_waitlist_capacity": true,
        "default_schedule_display_period": null,
        "late_cancel_policy": null,
        "waitlist_policy": null,
        "no_show_fee": "0.0",
        "late_cancel_fee": "0.0",
        "location_tax_categories": [

        ]
      }
    ]
  }
}
```



# Business Staff

Anyone who works for a Business Account. Most commonly, you'll want to get a list of instructors teaching classes.

## Filter By Role


### Request

#### Endpoint

```plaintext
GET /api/business_staffs?roles[]=instructor
Origin: http://mohr-sipes-and-keebler.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/business_staffs`

#### Parameters


```json
roles: [&quot;instructor&quot;]
```


| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| q  | Search by Name |
| roles  | List of roles to filter by |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;5f900f6754ac95fc659986f70c68e516&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: e741d248-8294-46ea-b84d-fc5bae549e6e
X-Runtime: 0.010479
Content-Length: 945
200 OK
```


```json
{
  "business_staffs": [
    {
      "id": "cac2df17-5a4b-4fe9-ad41-bafadc7eacaf",
      "email": "ila@franeckiferry.us",
      "slug": "ivana-will",
      "first_name": "Ivana",
      "last_name": "Will",
      "description": null,
      "hire_date": null,
      "phone": null,
      "is_kiosk": false,
      "active": true,
      "dob": null,
      "social_security_number": null,
      "address1": null,
      "address2": null,
      "city": null,
      "state": null,
      "zip_code": null,
      "emergency_contact_name": null,
      "emergency_contact_phone": null,
      "notes": null
    },
    {
      "id": "39b777cf-c5db-41ad-9ed3-f5a146056798",
      "email": "chang_veum@bradtke.info",
      "slug": "troy-mueller",
      "first_name": "Troy",
      "last_name": "Mueller",
      "description": null,
      "hire_date": null,
      "phone": null,
      "is_kiosk": false,
      "active": true,
      "dob": null,
      "social_security_number": null,
      "address1": null,
      "address2": null,
      "city": null,
      "state": null,
      "zip_code": null,
      "emergency_contact_name": null,
      "emergency_contact_phone": null,
      "notes": null
    }
  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 2,
    "per_page": 100
  }
}
```



## Get All


### Request

#### Endpoint

```plaintext
GET /api/business_staffs
Origin: http://olson-halvorson.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/business_staffs`

#### Parameters



| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| q  | Search by Name |
| roles  | List of roles to filter by |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;1fee4a7c1c37049c1c6bbbade6e1a864&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: eeb2efa2-cdd4-4d62-9f8e-176dafbc9557
X-Runtime: 0.020969
Content-Length: 1794
200 OK
```


```json
{
  "business_staffs": [
    {
      "id": "81ea798b-7fb3-4078-87f7-ca3131cdbdf5",
      "email": "wynell_terry@bartoletti.us",
      "slug": "elodia-paucek",
      "first_name": "Elodia",
      "last_name": "Paucek",
      "description": null,
      "hire_date": null,
      "phone": null,
      "is_kiosk": false,
      "active": true,
      "dob": null,
      "social_security_number": null,
      "address1": null,
      "address2": null,
      "city": null,
      "state": null,
      "zip_code": null,
      "emergency_contact_name": null,
      "emergency_contact_phone": null,
      "notes": null
    },
    {
      "id": "8a696635-d27e-4745-823c-5ff848226f25",
      "email": "felice_grimes@balistreri.biz",
      "slug": "kathleen-hahn",
      "first_name": "Kathleen",
      "last_name": "Hahn",
      "description": null,
      "hire_date": null,
      "phone": null,
      "is_kiosk": false,
      "active": true,
      "dob": null,
      "social_security_number": null,
      "address1": null,
      "address2": null,
      "city": null,
      "state": null,
      "zip_code": null,
      "emergency_contact_name": null,
      "emergency_contact_phone": null,
      "notes": null
    },
    {
      "id": "cd2be39a-de6e-4aef-a83c-5cdb8c2617cf",
      "email": "grover.simonis@kozey.us",
      "slug": "nery-gusikowski",
      "first_name": "Nery",
      "last_name": "Gusikowski",
      "description": null,
      "hire_date": null,
      "phone": null,
      "is_kiosk": false,
      "active": true,
      "dob": null,
      "social_security_number": null,
      "address1": null,
      "address2": null,
      "city": null,
      "state": null,
      "zip_code": null,
      "emergency_contact_name": null,
      "emergency_contact_phone": null,
      "notes": null
    },
    {
      "id": "ea3198e7-ca97-4ed2-8e5b-d8efc5bef638",
      "email": "cyril@bosco.co.uk",
      "slug": "darline-leannon",
      "first_name": "Darline",
      "last_name": "Leannon",
      "description": null,
      "hire_date": null,
      "phone": null,
      "is_kiosk": false,
      "active": true,
      "dob": null,
      "social_security_number": null,
      "address1": null,
      "address2": null,
      "city": null,
      "state": null,
      "zip_code": null,
      "emergency_contact_name": null,
      "emergency_contact_phone": null,
      "notes": null
    }
  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 4,
    "per_page": 100
  }
}
```



# Gift Cards

Can be redeemed for cash (account balance) or packages

## Redeem Cash Gift Card


### Request

#### Endpoint

```plaintext
POST /api/gift_cards/redeem
Origin: http://bergstrom-llc.mgrapp.com
Authorization: Bearer 00ceba50-c73f-4895-8182-7fb18a7a9f5b
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/gift_cards/redeem`

#### Parameters


```json
code=3F86787B
```


| Name | Description |
|:-----|:------------|
| code *required* | Gift Card Code |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;74da24326d3bd549ebbd83e2a2c4b9ef&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: a2633d01-afb0-4bf2-a828-0b59d3d1c3fd
X-Runtime: 0.127925
Content-Length: 1634
201 Created
```


```json
{
  "gift_card_instance": {
    "id": "9c211387-db6a-4f33-b0b7-c286b0357db4",
    "gift_card_type": "cash",
    "amount": "22.0",
    "code": "3F86787B",
    "num_sessions": 0,
    "created_at": "2019-06-09T14:27:09.004Z",
    "redeemed_at": "2019-06-09T14:27:09.041Z",
    "redeemer": {
      "email": "tommie@stracke.us"
    }
  },
  "transaction": {
    "id": "a0d9002d-cb79-4b53-85b1-7d0612dfe309",
    "created_at": "2019-06-09T14:27:09.094Z",
    "state": "complete",
    "amount": -22.0,
    "fail_message": null,
    "process_after": null,
    "processed_at": "2019-06-09T14:27:09.114Z",
    "payment_type": "account_balance",
    "description": null,
    "payment_source_invalid": false,
    "creator_type": null,
    "user_profile_id": "1fc4aee8-3499-4936-aa3a-867a468e18dc"
  },
  "package_instance": null,
  "user_profile": {
    "id": "1fc4aee8-3499-4936-aa3a-867a468e18dc",
    "account_balance": "122.0",
    "signed_waiver_at": null,
    "waiver_signer": null,
    "waiver_text": null,
    "created_at": "2019-06-09T14:27:09.017Z",
    "email": "tommie@stracke.us",
    "first_name": "Chong",
    "last_name": "Bednar",
    "address1": null,
    "address2": null,
    "city": null,
    "state": null,
    "zip_code": null,
    "phone": null,
    "dob": null,
    "gender": null,
    "default_stripe_source_id": null,
    "home_location_id": null,
    "referral_method": null,
    "referral_extra_info": null,
    "classpass_user_id": null,
    "member_start_date": "2019-06-09",
    "password_reset_required": false,
    "emergency_contact_name": null,
    "emergency_contact_phone": null,
    "send_account_management_email": true,
    "send_account_management_sms": true,
    "send_reservation_confirmation_email": true,
    "send_reservation_reminder_email": true,
    "send_reservation_reminder_sms": true,
    "send_promo_and_discount_email": true,
    "send_promo_and_discount_sms": true,
    "send_studio_communication_email": true,
    "send_studio_communication_sms": true
  }
}
```



# Offerings

Specific instances of a class that a user can sign up for

## Filter By Location


### Request

#### Endpoint

```plaintext
GET /api/offerings?time_zone_offset=420&amp;location_id=86183cf1-61bf-4b73-ab47-4098a2ab1188
Origin: http://klein-rodriguez-and-dibbert.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/offerings`

#### Parameters


```json
time_zone_offset: 420
location_id: 86183cf1-61bf-4b73-ab47-4098a2ab1188
```


| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| time_zone_offset  | Time Zone Offset, since time zones might matter |
| start_date  | Filter by date (inclusive) |
| end_date  | Filter by date (inclusive) |
| resource_id  | Filter by resource |
| business_staff_id  | Filter by instructor (or sub) |
| location_id  | Filter by location |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;0d37122dc74889ed996b34c9a6c311b4&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 72ae0778-0af0-4e2e-87b1-125bf6c15372
X-Runtime: 0.009486
Content-Length: 3062
200 OK
```


```json
{
  "offerings": [
    {
      "id": "01892d71-30f4-44e7-8b0f-47259788cd35",
      "resource_id": "683e268e-1447-4c13-8072-5cae77754c5d",
      "recurrence_id": null,
      "state": "active",
      "start_time": "2018-08-21T09:00:00.000Z",
      "end_time": "2018-08-21T10:00:00.000Z",
      "reservation_cutoff_time": "2018-08-21T09:00:00.000Z",
      "reservation_cutoff_time_in_minutes": 0,
      "waitlist_cutoff_time": "2018-08-21T09:00:00.000Z",
      "waitlist_cutoff_time_in_minutes": 0,
      "late_cancel_cutoff_time": "2018-08-21T09:00:00.000Z",
      "late_cancel_cutoff_time_in_minutes": 0,
      "late_cancel_grace_period_in_minutes": 0,
      "waitlist_allowed": true,
      "waitlist_capacity": 0,
      "num_waitlist_reservations": 0,
      "normal_capacity": 1,
      "num_normal_reservations": 0,
      "location_id": "86183cf1-61bf-4b73-ab47-4098a2ab1188",
      "business_staff_id": "c93f986f-3783-441d-a208-051182272bfb",
      "on_classpass": false,
      "publically_visible": true,
      "end_of_day_closeout_complete": false,
      "pay_rate_id": null,
      "waitlist_closing_complete": false,
      "substitute_id": null,
      "instructor_id": "c93f986f-3783-441d-a208-051182272bfb"
    },
    {
      "id": "519012c4-9446-494b-b0b8-15fa19cc37b9",
      "resource_id": "010dec7c-a34a-453f-bb91-47fd6e26dae9",
      "recurrence_id": null,
      "state": "active",
      "start_time": "2018-08-22T05:00:00.000Z",
      "end_time": "2018-08-22T06:00:00.000Z",
      "reservation_cutoff_time": "2018-08-22T05:00:00.000Z",
      "reservation_cutoff_time_in_minutes": 0,
      "waitlist_cutoff_time": "2018-08-22T05:00:00.000Z",
      "waitlist_cutoff_time_in_minutes": 0,
      "late_cancel_cutoff_time": "2018-08-22T05:00:00.000Z",
      "late_cancel_cutoff_time_in_minutes": 0,
      "late_cancel_grace_period_in_minutes": 0,
      "waitlist_allowed": true,
      "waitlist_capacity": 0,
      "num_waitlist_reservations": 0,
      "normal_capacity": 1,
      "num_normal_reservations": 0,
      "location_id": "86183cf1-61bf-4b73-ab47-4098a2ab1188",
      "business_staff_id": "0a90cf04-336e-4e65-a96a-50495e40956e",
      "on_classpass": false,
      "publically_visible": true,
      "end_of_day_closeout_complete": false,
      "pay_rate_id": null,
      "waitlist_closing_complete": false,
      "substitute_id": null,
      "instructor_id": "0a90cf04-336e-4e65-a96a-50495e40956e"
    },
    {
      "id": "6ecbfdcf-54c0-44d2-8b66-d1ebeb230fbe",
      "resource_id": "683e268e-1447-4c13-8072-5cae77754c5d",
      "recurrence_id": null,
      "state": "active",
      "start_time": "2018-08-22T17:00:00.000Z",
      "end_time": "2018-08-22T18:00:00.000Z",
      "reservation_cutoff_time": "2018-08-22T17:00:00.000Z",
      "reservation_cutoff_time_in_minutes": 0,
      "waitlist_cutoff_time": "2018-08-22T17:00:00.000Z",
      "waitlist_cutoff_time_in_minutes": 0,
      "late_cancel_cutoff_time": "2018-08-22T17:00:00.000Z",
      "late_cancel_cutoff_time_in_minutes": 0,
      "late_cancel_grace_period_in_minutes": 0,
      "waitlist_allowed": true,
      "waitlist_capacity": 0,
      "num_waitlist_reservations": 0,
      "normal_capacity": 1,
      "num_normal_reservations": 0,
      "location_id": "86183cf1-61bf-4b73-ab47-4098a2ab1188",
      "business_staff_id": "c9508dcb-cd29-476e-bf1e-c932f8af6902",
      "on_classpass": false,
      "publically_visible": true,
      "end_of_day_closeout_complete": false,
      "pay_rate_id": null,
      "waitlist_closing_complete": false,
      "substitute_id": null,
      "instructor_id": "c9508dcb-cd29-476e-bf1e-c932f8af6902"
    }
  ],
  "reservations": [

  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 3,
    "per_page": 100
  }
}
```



## Get All


### Request

#### Endpoint

```plaintext
GET /api/offerings?time_zone_offset=420
Origin: http://kohler-llc.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/offerings`

#### Parameters


```json
time_zone_offset: 420
```


| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| time_zone_offset  | Time Zone Offset, since time zones might matter |
| start_date  | Filter by date (inclusive) |
| end_date  | Filter by date (inclusive) |
| resource_id  | Filter by resource |
| business_staff_id  | Filter by instructor (or sub) |
| location_id  | Filter by location |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;e791c5730e86870ba21c313604af24ed&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: f2b5f54c-a577-44b7-9fda-ba30f0c31bc5
X-Runtime: 0.027937
Content-Length: 3062
200 OK
```


```json
{
  "offerings": [
    {
      "id": "c0a97f90-69a6-4860-a438-c0e817863094",
      "resource_id": "577b807a-22b8-4d5f-8781-f46f2ebdc29f",
      "recurrence_id": null,
      "state": "active",
      "start_time": "2018-08-21T09:00:00.000Z",
      "end_time": "2018-08-21T10:00:00.000Z",
      "reservation_cutoff_time": "2018-08-21T09:00:00.000Z",
      "reservation_cutoff_time_in_minutes": 0,
      "waitlist_cutoff_time": "2018-08-21T09:00:00.000Z",
      "waitlist_cutoff_time_in_minutes": 0,
      "late_cancel_cutoff_time": "2018-08-21T09:00:00.000Z",
      "late_cancel_cutoff_time_in_minutes": 0,
      "late_cancel_grace_period_in_minutes": 0,
      "waitlist_allowed": true,
      "waitlist_capacity": 0,
      "num_waitlist_reservations": 0,
      "normal_capacity": 1,
      "num_normal_reservations": 0,
      "location_id": "2971cfde-5bc2-4a84-83d8-840b9fd9652e",
      "business_staff_id": "cb932f32-c120-4703-bfde-46ed227ee81a",
      "on_classpass": false,
      "publically_visible": true,
      "end_of_day_closeout_complete": false,
      "pay_rate_id": null,
      "waitlist_closing_complete": false,
      "substitute_id": null,
      "instructor_id": "cb932f32-c120-4703-bfde-46ed227ee81a"
    },
    {
      "id": "160cac32-8697-4b5c-acee-d88e7704184a",
      "resource_id": "eb151bd3-8318-4094-8093-713ef226b7dd",
      "recurrence_id": null,
      "state": "active",
      "start_time": "2018-08-22T05:00:00.000Z",
      "end_time": "2018-08-22T06:00:00.000Z",
      "reservation_cutoff_time": "2018-08-22T05:00:00.000Z",
      "reservation_cutoff_time_in_minutes": 0,
      "waitlist_cutoff_time": "2018-08-22T05:00:00.000Z",
      "waitlist_cutoff_time_in_minutes": 0,
      "late_cancel_cutoff_time": "2018-08-22T05:00:00.000Z",
      "late_cancel_cutoff_time_in_minutes": 0,
      "late_cancel_grace_period_in_minutes": 0,
      "waitlist_allowed": true,
      "waitlist_capacity": 0,
      "num_waitlist_reservations": 0,
      "normal_capacity": 1,
      "num_normal_reservations": 0,
      "location_id": "2971cfde-5bc2-4a84-83d8-840b9fd9652e",
      "business_staff_id": "a25c6396-bf50-4cc3-8f1a-e5cb4ff7b08b",
      "on_classpass": false,
      "publically_visible": true,
      "end_of_day_closeout_complete": false,
      "pay_rate_id": null,
      "waitlist_closing_complete": false,
      "substitute_id": null,
      "instructor_id": "a25c6396-bf50-4cc3-8f1a-e5cb4ff7b08b"
    },
    {
      "id": "e863271a-e84b-4d9e-b130-cff146cf632f",
      "resource_id": "577b807a-22b8-4d5f-8781-f46f2ebdc29f",
      "recurrence_id": null,
      "state": "active",
      "start_time": "2018-08-22T17:00:00.000Z",
      "end_time": "2018-08-22T18:00:00.000Z",
      "reservation_cutoff_time": "2018-08-22T17:00:00.000Z",
      "reservation_cutoff_time_in_minutes": 0,
      "waitlist_cutoff_time": "2018-08-22T17:00:00.000Z",
      "waitlist_cutoff_time_in_minutes": 0,
      "late_cancel_cutoff_time": "2018-08-22T17:00:00.000Z",
      "late_cancel_cutoff_time_in_minutes": 0,
      "late_cancel_grace_period_in_minutes": 0,
      "waitlist_allowed": true,
      "waitlist_capacity": 0,
      "num_waitlist_reservations": 0,
      "normal_capacity": 1,
      "num_normal_reservations": 0,
      "location_id": "2971cfde-5bc2-4a84-83d8-840b9fd9652e",
      "business_staff_id": "772ed53c-967b-4512-b12b-40a93210ff58",
      "on_classpass": false,
      "publically_visible": true,
      "end_of_day_closeout_complete": false,
      "pay_rate_id": null,
      "waitlist_closing_complete": false,
      "substitute_id": null,
      "instructor_id": "772ed53c-967b-4512-b12b-40a93210ff58"
    }
  ],
  "reservations": [

  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 3,
    "per_page": 100
  }
}
```



# Orders

Purchasing one or more items

## Buying a Package


### Request

#### Endpoint

```plaintext
POST /api/orders
Origin: http://kuhic-lemke-and-macejkovic.mgrapp.com
Authorization: Bearer 11003c77-3d46-4e3b-bbfb-c1982bc06b2d
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/orders`

#### Parameters


```json
line_items[][variant_id]=154cb59b-499d-40cf-ae12-e470890f21b2&line_items[][quantity]=1&payments[][payment_type]=stripe_cc&payments[][source_id]=test_cc_2
```


| Name | Description |
|:-----|:------------|
| line_items *required* | List of items ({variant_id:, quantity:}) |
| payments *required* | List of payments ({payment_type:, source_id:}) |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;e042ceb33c01291ad5388f1fa91a15fd&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: af5bbc44-ac2d-42a9-830a-8ce6fea558cd
X-Runtime: 0.278206
Content-Length: 267
201 Created
```


```json
{
  "order": {
    "id": "fd9e1d5d-0f1f-409d-98b8-b6f41b5d2edf",
    "number": "fd9e1d5d",
    "created_at": "2019-06-09T14:27:09.322Z",
    "total": 0.0,
    "item_total": 8.0,
    "sales_tax_total": 0.0,
    "adjustment_total": 0.0,
    "payment_total": 8.0,
    "payment_state": "complete",
    "fulfillment_state": "complete"
  }
}
```



# Payment Methods

Ways in which a user can pay for services. Currently just Stripe credit cards and account balance.

## Create New


### Request

#### Endpoint

```plaintext
POST /api/payment_methods
Origin: http://marvin-altenwerth.mgrapp.com
Authorization: Bearer 6d5639ed-cb04-437e-800b-ad2518cb32b6
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/payment_methods`

#### Parameters


```json
stripe_token=test_tok_1
```


| Name | Description |
|:-----|:------------|
| stripe_token *required* | Token returned by Stripe SDK |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;1871ebb82d313d3092d09e1f38d7621c&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: aeb4e84a-d26d-408b-8679-29163667e292
X-Runtime: 0.075564
Content-Length: 227
201 Created
```


```json
{
  "payment_method": {
    "id": "test_cc_2",
    "source_id": "test_cc_2",
    "payment_type": "stripe_cc",
    "brand": "Visa",
    "exp_month": 9,
    "exp_year": 2018,
    "address_zip": null,
    "last4": "4242",
    "balance": 0.0,
    "is_default": true,
    "name_on_card": "Johnny App"
  }
}
```



## Get Available


### Request

#### Endpoint

```plaintext
GET /api/payment_methods
Origin: http://streich-hansen.mgrapp.com
Authorization: Bearer 4357dd52-d425-43ca-9b8b-89760443f1e3
Host: example.org
Cookie: 
```

`GET /api/payment_methods`

#### Parameters


None known.


### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;b077ec2b40497208207deaff9eb92559&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: ed388491-e1c1-48f1-a35c-431638f93993
X-Runtime: 0.016918
Content-Length: 422
200 OK
```


```json
{
  "payment_methods": [
    {
      "id": "test_cc_2",
      "source_id": "test_cc_2",
      "payment_type": "stripe_cc",
      "brand": "Visa",
      "exp_month": 11,
      "exp_year": 2099,
      "address_zip": null,
      "last4": "1234",
      "balance": 0.0,
      "is_default": true,
      "name_on_card": "Johnny App"
    },
    {
      "id": 0,
      "source_id": null,
      "payment_type": "account_balance",
      "brand": null,
      "exp_month": null,
      "exp_year": null,
      "address_zip": null,
      "last4": null,
      "balance": 100.0,
      "is_default": null,
      "name_on_card": null
    }
  ]
}
```



# Products

Anything that can be purchased by a user. Includes packages, gift cards, and physical items.

## Filter By Type


### Request

#### Endpoint

```plaintext
GET /api/products?types[]=package
Origin: http://rosenbaum-and-sons.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/products`

#### Parameters


```json
types: [&quot;package&quot;]
```


| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| q  | Search by Name |
| types  | Filter by Product Type |
| resource_offering_id  | Filter packages by applicability to given offering |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;97ffc3dd2a04ae293aaa5da391bace47&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 5d78dc8b-58dc-411d-8bc9-ce9877320ce2
X-Runtime: 0.017213
Content-Length: 2085
200 OK
```


```json
{
  "products": [
    {
      "id": "14d7acb2-2d18-4556-b25c-061a3a490f34",
      "name": "Trisync Digital Amplifier",
      "slug": "trisync-digital-amplifier",
      "description": null,
      "product_type": "package",
      "revenue_category_id": "de1975eb-d789-4032-bc45-9d509d5901e8",
      "tax_category_id": null,
      "available": true,
      "available_online": true,
      "is_favorite": false,
      "purchase_limit": null,
      "must_be_first_purchase": false,
      "package": {
        "id": "adaf7ada-7d4b-4c7e-8275-fbfcab752689",
        "unlimited_sessions": false,
        "num_sessions": 10,
        "expiration_type": "none",
        "expiration_unit": null,
        "expiration_period": null,
        "advance_schedule_in_days": null,
        "shareable": false,
        "for_guest_only": false,
        "guests_allowed": true,
        "waitlist_priority": 1,
        "is_recurring": false,
        "recurrence_period": null,
        "recurrence_unit": null,
        "recurring_price": null,
        "recurrence_minimum_count": null,
        "renewal_price": null,
        "recurrence_termination_type": null
      },
      "gift_card": null,
      "challenge_entry": null,
      "variants": [
        {
          "id": "60119e44-b30b-4f70-9be7-21225a95f64c",
          "price": 74.0,
          "is_master": true
        }
      ],
      "price": 74.0
    },
    {
      "id": "9a00be2e-a95a-4394-b49d-1619e35ddd28",
      "name": "Trestforge Performance Input Adapter",
      "slug": "trestforge-performance-input-adapter",
      "description": null,
      "product_type": "package",
      "revenue_category_id": "c9de5c30-810c-4962-8aa9-c0d6e727e106",
      "tax_category_id": null,
      "available": true,
      "available_online": true,
      "is_favorite": false,
      "purchase_limit": null,
      "must_be_first_purchase": false,
      "package": {
        "id": "558d7ebc-530e-4648-ae8d-df90047fa6b0",
        "unlimited_sessions": false,
        "num_sessions": 10,
        "expiration_type": "none",
        "expiration_unit": null,
        "expiration_period": null,
        "advance_schedule_in_days": null,
        "shareable": false,
        "for_guest_only": false,
        "guests_allowed": true,
        "waitlist_priority": 1,
        "is_recurring": false,
        "recurrence_period": null,
        "recurrence_unit": null,
        "recurring_price": null,
        "recurrence_minimum_count": null,
        "renewal_price": null,
        "recurrence_termination_type": null
      },
      "gift_card": null,
      "challenge_entry": null,
      "variants": [
        {
          "id": "75ef80a0-5ea5-4926-91d9-f9640fe8bb5f",
          "price": 49.0,
          "is_master": true
        }
      ],
      "price": 49.0
    }
  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 2,
    "per_page": 100
  }
}
```



## Get All


### Request

#### Endpoint

```plaintext
GET /api/products
Origin: http://bahringer-hayes.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/products`

#### Parameters



| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| q  | Search by Name |
| types  | Filter by Product Type |
| resource_offering_id  | Filter packages by applicability to given offering |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;0978186ab9b9d2a998f0d5addd4f2f0d&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 7dcda6a1-fa8e-4e78-b8b4-b95fc13ce582
X-Runtime: 0.095837
Content-Length: 3706
200 OK
```


```json
{
  "products": [
    {
      "id": "fb38fd27-3538-4d87-9f41-0aaa2e905fe2",
      "name": "Cafunc Gel Digital Amplifier",
      "slug": "cafunc-gel-digital-amplifier",
      "description": null,
      "product_type": "gift_card",
      "revenue_category_id": "19eb7fdc-12a4-4322-9c48-3936549a5753",
      "tax_category_id": null,
      "available": true,
      "available_online": true,
      "is_favorite": false,
      "purchase_limit": null,
      "must_be_first_purchase": false,
      "package": null,
      "gift_card": {
        "id": "c9a3d003-0fa4-4026-ba24-4ffbd3caeb26",
        "gift_card_type": "cash",
        "fixed_amount": true,
        "amount": "20.0",
        "num_sessions": 0
      },
      "challenge_entry": null,
      "variants": [
        {
          "id": "488312ec-a0ae-47db-8b2c-236f089c71a6",
          "price": 59.0,
          "is_master": true
        }
      ],
      "price": 59.0
    },
    {
      "id": "3827b43a-dbf1-4bd9-9d70-76283b478a30",
      "name": "Cygcell Portable Mount",
      "slug": "cygcell-portable-mount",
      "description": null,
      "product_type": "package",
      "revenue_category_id": "850cd407-bc77-49fb-84c9-dff06fa2868e",
      "tax_category_id": null,
      "available": true,
      "available_online": true,
      "is_favorite": false,
      "purchase_limit": null,
      "must_be_first_purchase": false,
      "package": {
        "id": "0ab5010f-68c8-44ef-a67f-c7e88604bcd5",
        "unlimited_sessions": false,
        "num_sessions": 10,
        "expiration_type": "none",
        "expiration_unit": null,
        "expiration_period": null,
        "advance_schedule_in_days": null,
        "shareable": false,
        "for_guest_only": false,
        "guests_allowed": true,
        "waitlist_priority": 1,
        "is_recurring": false,
        "recurrence_period": null,
        "recurrence_unit": null,
        "recurring_price": null,
        "recurrence_minimum_count": null,
        "renewal_price": null,
        "recurrence_termination_type": null
      },
      "gift_card": null,
      "challenge_entry": null,
      "variants": [
        {
          "id": "f7ec9069-3d8d-4aba-87be-19f8152e2442",
          "price": 75.0,
          "is_master": true
        }
      ],
      "price": 75.0
    },
    {
      "id": "8f479e3c-d1ae-4a1e-a9f9-1d9d8416498d",
      "name": "DFA Air Remote Kit",
      "slug": "dfa-air-remote-kit",
      "description": null,
      "product_type": "package",
      "revenue_category_id": "cb2aa870-3ab7-4315-b307-2989b2360574",
      "tax_category_id": null,
      "available": true,
      "available_online": true,
      "is_favorite": false,
      "purchase_limit": null,
      "must_be_first_purchase": false,
      "package": {
        "id": "86652aea-021b-43e0-a293-9c00a1b48448",
        "unlimited_sessions": false,
        "num_sessions": 10,
        "expiration_type": "none",
        "expiration_unit": null,
        "expiration_period": null,
        "advance_schedule_in_days": null,
        "shareable": false,
        "for_guest_only": false,
        "guests_allowed": true,
        "waitlist_priority": 1,
        "is_recurring": false,
        "recurrence_period": null,
        "recurrence_unit": null,
        "recurring_price": null,
        "recurrence_minimum_count": null,
        "renewal_price": null,
        "recurrence_termination_type": null
      },
      "gift_card": null,
      "challenge_entry": null,
      "variants": [
        {
          "id": "609d6609-0ae8-4a9d-9572-f2cf42926208",
          "price": 24.0,
          "is_master": true
        }
      ],
      "price": 24.0
    },
    {
      "id": "62833aa6-f83a-45ff-b659-b03eb89995ed",
      "name": "Bruphfunc Air Filter",
      "slug": "bruphfunc-air-filter",
      "description": null,
      "product_type": "normal",
      "revenue_category_id": "adc1db8c-a2ee-4788-bef2-61099ff9cf5a",
      "tax_category_id": null,
      "available": true,
      "available_online": true,
      "is_favorite": false,
      "purchase_limit": null,
      "must_be_first_purchase": false,
      "package": null,
      "gift_card": null,
      "challenge_entry": null,
      "variants": [
        {
          "id": "dff8c15b-df7a-4496-9fb3-d4f59a680f68",
          "price": 56.0,
          "is_master": true
        }
      ],
      "price": 56.0
    },
    {
      "id": "daf11daf-41a0-4c84-82b9-a9c9a682594a",
      "name": "Onecell Disc Digital Bridge",
      "slug": "onecell-disc-digital-bridge",
      "description": null,
      "product_type": "normal",
      "revenue_category_id": "6f2022ee-9d69-4399-94d2-5e2995406172",
      "tax_category_id": null,
      "available": true,
      "available_online": true,
      "is_favorite": false,
      "purchase_limit": null,
      "must_be_first_purchase": false,
      "package": null,
      "gift_card": null,
      "challenge_entry": null,
      "variants": [
        {
          "id": "03223ac2-0971-4b8a-a527-8640f58bc6e4",
          "price": 24.0,
          "is_master": true
        }
      ],
      "price": 24.0
    }
  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 5,
    "per_page": 100
  }
}
```



# Reservations

Specific instance of a user signing up for an offering

## Create New


### Request

#### Endpoint

```plaintext
POST /api/reservations
Origin: http://buckridge-marks-and-mclaughlin.mgrapp.com
Authorization: Bearer c75558f5-9068-4fb8-930f-d4ab46fdf6ae
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/reservations`

#### Parameters


```json
reservations[][resource_offering_id]=e1798a0d-2ac2-4a3f-b26d-a44644a8f6e2&reservations[][package_instance_id]=584aa807-76c0-4f31-9ff3-cc29cbe6e55f
```


| Name | Description |
|:-----|:------------|
| reservations[resource_offering_id] *required* | Id of offering to sign up for |
| reservations[package_instance_id] *required* | Id of package used to pay for reservation |
| reservations[is_guest]  | Reservation is for a guest? |
| reservations[guest_name]  | Guest Name |
| reservations[guest_email]  | Guest Email |
| reservations[guest_phone]  | Guest Phone |
| reservations[accepts_waiver]  | If user accepts waiver |
| reservations[note]  | Note to the instructor |
| reservations[recurrence][start_date]  | Recurrence Start Date |
| reservations[recurrence][end_date]  | Recurrence End Date |
| reservations[recurrence][on_monday]  | Include Monday recurrences |
| reservations[recurrence][on_tuesday]  | Include Tuesday recurrences |
| reservations[recurrence][on_wednesday]  | Include Wednesday recurrences |
| reservations[recurrence][on_thursday]  | Include Thursday recurrences |
| reservations[recurrence][on_friday]  | Include Friday recurrences |
| reservations[recurrence][on_saturday]  | Include Saturday recurrences |
| reservations[recurrence][on_sunday]  | Include Sunday recurrences |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;ccf9e3553b7de352aca8b18dca37ba10&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 629c33b6-bf3b-434d-8835-484def9b1da1
X-Runtime: 0.150467
Content-Length: 2175
201 Created
```


```json
{
  "reservations": [
    {
      "id": "0d80cfee-0c19-428f-a612-50264c17b48d",
      "state": "reserved",
      "prev_state": null,
      "created_at": "2019-06-09T14:27:10.064Z",
      "state_change_at": null,
      "offering_id": "e1798a0d-2ac2-4a3f-b26d-a44644a8f6e2",
      "package_instance_id": "584aa807-76c0-4f31-9ff3-cc29cbe6e55f",
      "is_guest": false,
      "is_no_show": false,
      "is_late_cancel": false,
      "time_zone": "America/Los_Angeles",
      "start_time": "2019-06-09T15:27:09.927Z",
      "waitlist_promoted_at": null,
      "signed_in_at": null,
      "user_id": "67f1be49-8f85-4ea6-b305-f58174eecb61",
      "classpass_id": null,
      "guest_email": null,
      "guest_name": null,
      "guest_phone": null,
      "note": null
    }
  ],
  "offerings": [
    {
      "id": "e1798a0d-2ac2-4a3f-b26d-a44644a8f6e2",
      "resource_id": "9a9c3da3-8f1d-4fac-a32f-5f5d84f1436e",
      "recurrence_id": null,
      "state": "active",
      "start_time": "2019-06-09T15:27:09.927Z",
      "end_time": "2019-06-09T16:27:09.927Z",
      "reservation_cutoff_time": "2019-06-09T15:27:09.927Z",
      "reservation_cutoff_time_in_minutes": 0,
      "waitlist_cutoff_time": "2019-06-09T15:27:09.927Z",
      "waitlist_cutoff_time_in_minutes": 0,
      "late_cancel_cutoff_time": "2019-06-09T15:27:09.927Z",
      "late_cancel_cutoff_time_in_minutes": 0,
      "late_cancel_grace_period_in_minutes": 0,
      "waitlist_allowed": true,
      "waitlist_capacity": 0,
      "num_waitlist_reservations": 0,
      "normal_capacity": 10,
      "num_normal_reservations": 1,
      "location_id": "edbe72f5-32d4-404a-99b6-51132e4a8505",
      "business_staff_id": "61e32e9a-60ad-40cc-a525-cb76ce2ef052",
      "on_classpass": false,
      "publically_visible": true,
      "end_of_day_closeout_complete": false,
      "pay_rate_id": null,
      "waitlist_closing_complete": false,
      "substitute_id": null,
      "instructor_id": "61e32e9a-60ad-40cc-a525-cb76ce2ef052"
    }
  ],
  "packages": [
    {
      "id": "584aa807-76c0-4f31-9ff3-cc29cbe6e55f",
      "name": "Phunsfunc Digital Output Controller",
      "state": "active",
      "start_date": null,
      "end_date": null,
      "purchased_at": null,
      "unlimited_sessions": true,
      "total_sessions": 10,
      "sessions_remaining": 10,
      "created_at": "2019-06-09T14:27:09.882Z",
      "is_recurring": false,
      "expiration_type": "none",
      "expiration_unit": null,
      "expiration_period": null,
      "shareable": false,
      "guests_allowed": true,
      "for_guest_only": false,
      "waitlist_priority": 1,
      "advance_schedule_in_days": null,
      "recurring_user_package_id": null,
      "recurrence_unit": null,
      "recurrence_period": null
    }
  ],
  "missing": [

  ]
}
```



# Resource

A.K.A. Classes. A Resource is the generic type of a
thing (e.g. Pilates, Vinyasa Yoga). Whereas an Offering is the specific instance of
it (e.g. Pilates at 8am on July 14 with Sarah)


## Get All


### Request

#### Endpoint

```plaintext
GET /api/resources
Origin: http://rowe-group.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/resources`

#### Parameters



| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| q  | Search by Name |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;eb35e4b520b97878cfafb3ff177a2e9c&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 46bd76b7-5b0c-4494-8b08-07212f7133dc
X-Runtime: 0.033122
Content-Length: 1767
200 OK
```


```json
{
  "resources": [
    {
      "id": "bdd1c695-54e4-4be0-b8b6-037a114f7d43",
      "name": "Nutty Affineurs 3437ce78",
      "slug": "nutty-affineurs-3437ce78",
      "description": "So cute but cheesy say cheese 10 grilled cheese sandwiches you should try immediately with - tongue in cheek garlic cheese biscuits but poets have been mysteriously silent on the subject of cheese is like chalk and cheese trying too hard, unsubtle, and inauthentic of cheesy business lingo garlic cheese biscuits.",
      "resource_type": null,
      "pre_reservation_message": null,
      "post_reservation_message": null
    },
    {
      "id": "39a13e4a-8c8c-432d-8bad-b9f017d99a08",
      "name": "Cheesed Brie a3fe7a2d",
      "slug": "cheesed-brie-a3fe7a2d",
      "description": "So cute but cheesy it is blue sky thinking when the rennet is added, curds are formed applewood smoked coagulation of the milk protein casein but round cheeses are to be cut in wedges, like a cake say cheese cut the cheese of cheesy business lingo applewood smoked.",
      "resource_type": null,
      "pre_reservation_message": null,
      "post_reservation_message": null
    },
    {
      "id": "0d5f741f-8acc-4435-b31d-06fe50d24c91",
      "name": "Cheesed Coulommiers d8cb3be9",
      "slug": "cheesed-coulommiers-d8cb3be9",
      "description": "Until the wheels form a white coat of penicillium moulds until the wheels form a white coat of penicillium moulds Sheridans Cheesemongers the whiter and fresher the cheese, the crisper and fruitier the wine should be in an artisan farmerhouse blend the flour, cheese and they can also age quite well in ripening cellars where but poets have been mysteriously silent on the subject of cheese cut to size applewood smoked.",
      "resource_type": null,
      "pre_reservation_message": null,
      "post_reservation_message": null
    }
  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 3,
    "per_page": 100
  }
}
```



# User Account

User profile and account information

## Check Email


### Request

#### Endpoint

```plaintext
GET /api/users/check_email?email=gene.gerhold%40senger.com
Origin: http://lang-llc.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/users/check_email`

#### Parameters


```json
email: gene.gerhold@senger.com
```


| Name | Description |
|:-----|:------------|
| email *required* | Email |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;c821f1244fd68b10cc644a392beaf4d8&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 8f60c5ef-2f2a-4969-a6ec-24b088f979f1
X-Runtime: 0.011478
Content-Length: 34
200 OK
```


```json
{
  "exists": true,
  "phone_last4": null
}
```



## Get Session


### Request

#### Endpoint

```plaintext
GET /api/users/me
Origin: http://koepp-group.mgrapp.com
Authorization: Bearer 38782f8a-6acb-4baa-bbeb-24310f65f6ab
Host: example.org
Cookie: 
```

`GET /api/users/me`

#### Parameters


None known.


### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;745fe36699424617abe9a7dc2edf2093&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 9e0092fa-0c46-4f3f-bd53-76e7e950baaf
X-Runtime: 0.013656
Content-Length: 1071
200 OK
```


```json
{
  "session": {
    "id": "38782f8a-6acb-4baa-bbeb-24310f65f6ab",
    "expires_at": "2019-06-23T14:27:07.482Z"
  },
  "user": {
    "id": "80a457d2-fe38-4af3-ae93-0ec85ae256b1",
    "account_balance": "0.0",
    "signed_waiver_at": null,
    "waiver_signer": null,
    "waiver_text": null,
    "created_at": "2019-06-09T14:27:07.479Z",
    "email": "george_schmidt@bernierweissnat.us",
    "first_name": "Toby",
    "last_name": "Gerlach",
    "address1": null,
    "address2": null,
    "city": null,
    "state": null,
    "zip_code": null,
    "phone": null,
    "dob": null,
    "gender": null,
    "default_stripe_source_id": null,
    "home_location_id": null,
    "referral_method": null,
    "referral_extra_info": null,
    "classpass_user_id": null,
    "member_start_date": "2019-06-09",
    "password_reset_required": false,
    "emergency_contact_name": null,
    "emergency_contact_phone": null,
    "send_account_management_email": true,
    "send_account_management_sms": true,
    "send_reservation_confirmation_email": true,
    "send_reservation_reminder_email": true,
    "send_reservation_reminder_sms": true,
    "send_promo_and_discount_email": true,
    "send_promo_and_discount_sms": true,
    "send_studio_communication_email": true,
    "send_studio_communication_sms": true
  }
}
```



## Register


### Request

#### Endpoint

```plaintext
POST /api/users
Origin: http://price-group.mgrapp.com
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/users`

#### Parameters


```json
email=foo%40bar.com&password=password&first_name=Foo&last_name=Bar&address1=123+Fake+St.&address2=&city=Dallas&state=TX&zip_code=54682&phone=7896365485&dob=1980-01-01&accepts_waiver=1
```


| Name | Description |
|:-----|:------------|
| email *required* | Email |
| password *required* | Password |
| first_name *required* | First Name |
| last_name *required* | Last Name |
| address1  | Address |
| address2  | Address |
| city  | City |
| state  | State |
| zip_code  | Zip Code |
| phone  | Phone |
| dob  | Date of Birth |
| accepts_waiver  | Accepts waiver |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;6de29b827c8eec9659be4331e7f2a554&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: a151445b-8479-4e6d-b30f-809c78b8a692
X-Runtime: 0.052602
Content-Length: 1075
201 Created
```


```json
{
  "session": {
    "id": "692219d1-8d3c-4a4b-98ff-233dc556b3ed",
    "expires_at": null
  },
  "user": {
    "id": "53800785-222b-4ed6-912e-3df5860cc4a2",
    "account_balance": "0.0",
    "signed_waiver_at": "2019-06-09T14:27:07.782Z",
    "waiver_signer": null,
    "waiver_text": null,
    "created_at": "2019-06-09T14:27:07.800Z",
    "email": "foo@bar.com",
    "first_name": "Foo",
    "last_name": "Bar",
    "address1": "123 Fake St.",
    "address2": "",
    "city": "Dallas",
    "state": "TX",
    "zip_code": "54682",
    "phone": "7896365485",
    "dob": "1980-01-01",
    "gender": null,
    "default_stripe_source_id": null,
    "home_location_id": null,
    "referral_method": null,
    "referral_extra_info": null,
    "classpass_user_id": null,
    "member_start_date": "2019-06-09",
    "password_reset_required": false,
    "emergency_contact_name": null,
    "emergency_contact_phone": null,
    "send_account_management_email": true,
    "send_account_management_sms": true,
    "send_reservation_confirmation_email": true,
    "send_reservation_reminder_email": true,
    "send_reservation_reminder_sms": true,
    "send_promo_and_discount_email": true,
    "send_promo_and_discount_sms": true,
    "send_studio_communication_email": true,
    "send_studio_communication_sms": true
  }
}
```



## Request Password Reset Token


### Request

#### Endpoint

```plaintext
POST /api/users/password_reset_token
Origin: http://ortiz-kreiger.mgrapp.com
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/users/password_reset_token`

#### Parameters


```json
email=jona%40crona.co.uk
```


| Name | Description |
|:-----|:------------|
| email *required* | Email |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;44136fa355b3678a1146ad16f7e8649e&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: e5965fd8-d752-4259-bf11-095a7d494ba2
X-Runtime: 0.036542
Content-Length: 2
200 OK
```


```json
{
}
```



## Reset Password


### Request

#### Endpoint

```plaintext
POST /api/users/4199056b-76b3-4d97-8198-6b5c2eff8366/reset_password
Origin: http://torphy-inc.mgrapp.com
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/users/:user_id/reset_password`

#### Parameters


```json
password=new-password&old_password=password
```


| Name | Description |
|:-----|:------------|
| password *required* | Password Reset Token |
| old_password *required* | Password Reset Token |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;cd8ceb58bff398ac1e6700dcdfd0673f&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 833abe72-e740-49f6-b2fa-c6a0bf0b5cc8
X-Runtime: 0.028791
Content-Length: 1035
200 OK
```


```json
{
  "session": {
    "id": "b7eb041b-6833-4b8b-82f6-60eb04f20797",
    "expires_at": null
  },
  "user": {
    "id": "4199056b-76b3-4d97-8198-6b5c2eff8366",
    "account_balance": "0.0",
    "signed_waiver_at": null,
    "waiver_signer": null,
    "waiver_text": null,
    "created_at": "2019-06-09T14:27:07.562Z",
    "email": "nancie@goyettemann.ca",
    "first_name": "Annis",
    "last_name": "Huel",
    "address1": null,
    "address2": null,
    "city": null,
    "state": null,
    "zip_code": null,
    "phone": null,
    "dob": null,
    "gender": null,
    "default_stripe_source_id": null,
    "home_location_id": null,
    "referral_method": null,
    "referral_extra_info": null,
    "classpass_user_id": null,
    "member_start_date": "2019-06-09",
    "password_reset_required": false,
    "emergency_contact_name": null,
    "emergency_contact_phone": null,
    "send_account_management_email": true,
    "send_account_management_sms": true,
    "send_reservation_confirmation_email": true,
    "send_reservation_reminder_email": true,
    "send_reservation_reminder_sms": true,
    "send_promo_and_discount_email": true,
    "send_promo_and_discount_sms": true,
    "send_studio_communication_email": true,
    "send_studio_communication_sms": true
  }
}
```



## Send Email Verification Token


### Request

#### Endpoint

```plaintext
POST /api/users/send_email_verification_token
Origin: http://wuckert-west-and-schamberger.mgrapp.com
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/users/send_email_verification_token`

#### Parameters


```json
email=erick_pouros%40boscoauer.biz&send_via=email
```


| Name | Description |
|:-----|:------------|
| email *required* | Email |
| send_via *required* | Method to send by ("email" or "sms") |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;44136fa355b3678a1146ad16f7e8649e&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: f6bb17a4-ed6a-4105-818e-d4c822ae6a81
X-Runtime: 0.071754
Content-Length: 2
200 OK
```


```json
{
}
```



## Sign In


### Request

#### Endpoint

```plaintext
POST /api/users/session
Origin: http://connelly-reichel-and-hintz.mgrapp.com
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`POST /api/users/session`

#### Parameters


```json
email=spencer_bailey%40reichel.biz&password=password
```


| Name | Description |
|:-----|:------------|
| email *required* | Email |
| password *required* | Password |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;d4a4d78a2386b75cf0078880ad77651a&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 068a5536-5274-480d-a693-c2d00b7959f4
X-Runtime: 0.031699
Content-Length: 1042
201 Created
```


```json
{
  "session": {
    "id": "6166f950-9f20-45b0-bde2-f707051fee71",
    "expires_at": null
  },
  "user": {
    "id": "c4fb9f82-b874-4040-bb45-85a4d8841e34",
    "account_balance": "0.0",
    "signed_waiver_at": null,
    "waiver_signer": null,
    "waiver_text": null,
    "created_at": "2019-06-09T14:27:07.337Z",
    "email": "spencer_bailey@reichel.biz",
    "first_name": "Judith",
    "last_name": "Ebert",
    "address1": null,
    "address2": null,
    "city": null,
    "state": null,
    "zip_code": null,
    "phone": null,
    "dob": null,
    "gender": null,
    "default_stripe_source_id": null,
    "home_location_id": null,
    "referral_method": null,
    "referral_extra_info": null,
    "classpass_user_id": null,
    "member_start_date": "2019-06-09",
    "password_reset_required": false,
    "emergency_contact_name": null,
    "emergency_contact_phone": null,
    "send_account_management_email": true,
    "send_account_management_sms": true,
    "send_reservation_confirmation_email": true,
    "send_reservation_reminder_email": true,
    "send_reservation_reminder_sms": true,
    "send_promo_and_discount_email": true,
    "send_promo_and_discount_sms": true,
    "send_studio_communication_email": true,
    "send_studio_communication_sms": true
  }
}
```



## Sign Out


### Request

#### Endpoint

```plaintext
DELETE /api/users/session
Origin: http://eichmann-barrows-and-rogahn.mgrapp.com
Authorization: Bearer 0af4f8d9-20d8-42ff-aa15-81ff69c73205
Host: example.org
Content-Type: application/x-www-form-urlencoded
Cookie: 
```

`DELETE /api/users/session`

#### Parameters


None known.


### Response

```plaintext
Status: 200
Cache-Control: no-cache
X-Request-Id: 6cd0da73-143f-4fcd-8192-cefe8a88f23b
X-Runtime: 0.013501
204 No Content
```




## Verify Password Reset Token


### Request

#### Endpoint

```plaintext
GET /api/users/password_reset_token?token=e672fb5c0f7c1d4653b0ac3ce745aed3
Origin: http://schuppe-and-sons.mgrapp.com
Host: example.org
Cookie: 
```

`GET /api/users/password_reset_token`

#### Parameters


```json
token: e672fb5c0f7c1d4653b0ac3ce745aed3
```


| Name | Description |
|:-----|:------------|
| token *required* | Password Reset Token |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;cb7907fc605acc4c999c004520da2a7c&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 4a32d05b-5b42-4618-b507-b6314456d4a5
X-Runtime: 0.011679
Content-Length: 957
200 OK
```


```json
{
  "user": {
    "id": "66bb9c46-5da2-46d9-b7c0-57cba1a30445",
    "account_balance": "0.0",
    "signed_waiver_at": null,
    "waiver_signer": null,
    "waiver_text": null,
    "created_at": "2019-06-09T14:27:07.517Z",
    "email": "lucy@davis.us",
    "first_name": "Kittie",
    "last_name": "Steuber",
    "address1": null,
    "address2": null,
    "city": null,
    "state": null,
    "zip_code": null,
    "phone": null,
    "dob": null,
    "gender": null,
    "default_stripe_source_id": null,
    "home_location_id": null,
    "referral_method": null,
    "referral_extra_info": null,
    "classpass_user_id": null,
    "member_start_date": "2019-06-09",
    "password_reset_required": false,
    "emergency_contact_name": null,
    "emergency_contact_phone": null,
    "send_account_management_email": true,
    "send_account_management_sms": true,
    "send_reservation_confirmation_email": true,
    "send_reservation_reminder_email": true,
    "send_reservation_reminder_sms": true,
    "send_promo_and_discount_email": true,
    "send_promo_and_discount_sms": true,
    "send_studio_communication_email": true,
    "send_studio_communication_sms": true
  }
}
```



# User Package

Used by a client to book classes

## Get All


### Request

#### Endpoint

```plaintext
GET /api/user_packages
Origin: http://ratke-berge.mgrapp.com
Authorization: Bearer f6b291b6-8002-4647-ac8f-679db20d486d
Host: example.org
Cookie: 
```

`GET /api/user_packages`

#### Parameters



| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| active  | Filter by unexpired packages with non-zero sessions remaining (only|_null_) |
| shareable  | Filter by packages that can be shared with other users (only|exclude) |
| recurring  | Filter by recurring packages (only|exclude) |
| resource_offering_id  | Filter packages by applicability to given offering |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;0783fd9960cd41fc0b642a32998b80ac&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 2ed0e73d-27e5-4d77-97ce-3ce63666d197
X-Runtime: 0.052531
Content-Length: 1786
200 OK
```


```json
{
  "packages": [
    {
      "id": "e5dc2bd5-4e59-44b0-b01e-c922bd2960c5",
      "name": "Bruckwood HD Remote Adapter",
      "state": "active",
      "start_date": null,
      "end_date": null,
      "purchased_at": null,
      "unlimited_sessions": true,
      "total_sessions": 1,
      "sessions_remaining": 1,
      "created_at": "2019-06-09T14:27:08.424Z",
      "is_recurring": false,
      "expiration_type": "none",
      "expiration_unit": null,
      "expiration_period": null,
      "shareable": false,
      "guests_allowed": true,
      "for_guest_only": false,
      "waitlist_priority": 1,
      "advance_schedule_in_days": null,
      "recurring_user_package_id": null,
      "recurrence_unit": null,
      "recurrence_period": null
    },
    {
      "id": "f64197cb-9bd9-4bbe-a513-b37adefb99fe",
      "name": "Trieckwood Audible Electric Bridge",
      "state": "active",
      "start_date": null,
      "end_date": null,
      "purchased_at": null,
      "unlimited_sessions": true,
      "total_sessions": 1,
      "sessions_remaining": 1,
      "created_at": "2019-06-09T14:27:08.395Z",
      "is_recurring": false,
      "expiration_type": "none",
      "expiration_unit": null,
      "expiration_period": null,
      "shareable": false,
      "guests_allowed": true,
      "for_guest_only": false,
      "waitlist_priority": 1,
      "advance_schedule_in_days": null,
      "recurring_user_package_id": null,
      "recurrence_unit": null,
      "recurrence_period": null
    },
    {
      "id": "1608d4b1-ffb1-414d-b6ca-511f0cc3ee5b",
      "name": "Finbalt Disc Compressor",
      "state": "active",
      "start_date": null,
      "end_date": null,
      "purchased_at": null,
      "unlimited_sessions": true,
      "total_sessions": 1,
      "sessions_remaining": 1,
      "created_at": "2019-06-09T14:27:08.342Z",
      "is_recurring": false,
      "expiration_type": "none",
      "expiration_unit": null,
      "expiration_period": null,
      "shareable": false,
      "guests_allowed": true,
      "for_guest_only": false,
      "waitlist_priority": 1,
      "advance_schedule_in_days": null,
      "recurring_user_package_id": null,
      "recurrence_unit": null,
      "recurrence_period": null
    }
  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 3,
    "per_page": 100
  }
}
```



# User Transactions

Record of user debits, credits, account balance adjustments, etc. Basically anything that involves a change in money

## Get All


### Request

#### Endpoint

```plaintext
GET /api/transactions
Origin: http://zulauf-inc.mgrapp.com
Authorization: Bearer 4f2755d2-a129-47e9-824a-06648c255dd4
Host: example.org
Cookie: 
```

`GET /api/transactions`

#### Parameters



| Name | Description |
|:-----|:------------|
| page  | Page |
| per_page  | Per Page |
| start_date  | Filter by Start Date |
| end_date  | Filter by End Date |



### Response

```plaintext
Content-Type: application/json; charset=utf-8
ETag: W/&quot;6b90eb1583f9ea71d95015400853f31a&quot;
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 72bac04f-db00-49ec-96e9-77ad1c2f4286
X-Runtime: 0.020456
Content-Length: 1860
200 OK
```


```json
{
  "transactions": [
    {
      "id": "799546d7-10a2-416e-bd4a-32dc8efd7a45",
      "created_at": "2019-06-09T14:27:10.402Z",
      "state": "pending_capture",
      "amount": 28.0,
      "fail_message": null,
      "process_after": null,
      "processed_at": null,
      "payment_type": "account_balance",
      "description": null,
      "payment_source_invalid": false,
      "creator_type": null,
      "user_profile_id": "b484d192-bc54-4e6e-9fca-eaa2ec877276"
    },
    {
      "id": "78ef248b-bb20-4cd4-a11b-102ca9098d91",
      "created_at": "2019-06-09T14:27:10.399Z",
      "state": "pending_capture",
      "amount": 29.0,
      "fail_message": null,
      "process_after": null,
      "processed_at": null,
      "payment_type": "account_balance",
      "description": null,
      "payment_source_invalid": false,
      "creator_type": null,
      "user_profile_id": "b484d192-bc54-4e6e-9fca-eaa2ec877276"
    },
    {
      "id": "4ab7eb0d-26d4-405f-9f89-140c7a741873",
      "created_at": "2019-06-09T14:27:10.396Z",
      "state": "pending_capture",
      "amount": 92.0,
      "fail_message": null,
      "process_after": null,
      "processed_at": null,
      "payment_type": "account_balance",
      "description": null,
      "payment_source_invalid": false,
      "creator_type": null,
      "user_profile_id": "b484d192-bc54-4e6e-9fca-eaa2ec877276"
    },
    {
      "id": "3209c428-cdb1-41f0-8394-494bdb8f943e",
      "created_at": "2019-06-09T14:27:10.393Z",
      "state": "pending_capture",
      "amount": 88.0,
      "fail_message": null,
      "process_after": null,
      "processed_at": null,
      "payment_type": "account_balance",
      "description": null,
      "payment_source_invalid": false,
      "creator_type": null,
      "user_profile_id": "b484d192-bc54-4e6e-9fca-eaa2ec877276"
    },
    {
      "id": "a59c795e-7a40-4fac-82c9-c886bdee4439",
      "created_at": "2019-06-09T14:27:10.389Z",
      "state": "pending_capture",
      "amount": 78.0,
      "fail_message": null,
      "process_after": null,
      "processed_at": null,
      "payment_type": "account_balance",
      "description": null,
      "payment_source_invalid": false,
      "creator_type": null,
      "user_profile_id": "b484d192-bc54-4e6e-9fca-eaa2ec877276"
    }
  ],
  "pagination": {
    "curr_page": 1,
    "next_page": null,
    "prev_page": null,
    "max_page": 1,
    "total_count": 5,
    "per_page": 100
  }
}
```



