# JSON
https://en.wikipedia.org/wiki/JSON

``` json
{
  "firstName": "John",
  "lastName": "Smith",  # string
  "isAlive": true,  # boolean
  "age": 27,  # number
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [  # list
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],  # empty list
  "spouse": null,  # empty value
  "link": [
    "abc",
    [  # list of list
      "123",
      "234"
    ],
    "ghi"
  ]
}
```


# YAML
https://en.wikipedia.org/wiki/YAML

``` yaml
---  # demo
firstName: John  # comments part of YAML
lastName: Smith
isAlive: true
age: 27
address:
  streetAddress: 21 2nd Street
  city: New York
  state: NY
  postalCode: 10021-3100
phoneNumbers:
- type: home  # list start with "-"
  number: 212 555-1234
- type: office
  number: 646 555-4567
children: []
spouse:
link:
- abc
- - '123'
  - '234'
- ['123', '234']  # is also a proper list
- ghi
data: |
  Multi-line strings is possible
  by including the pipe character.
```


# TOML
https://en.wikipedia.org/wiki/TOML

`key = "value"` pairs with `[section_names]` and `# comments`. Resembles `.ini` files. No spaces allowed in section names


``` toml
+++
firstName = "John"
lastName = "Smith"
isAlive = true
age = 27
children = [ ]
link = [ "abc", "ghi" ]

[address]
streetAddress = "21 2nd Street"
city = "New York"
state = "NY"
postalCode = "10021-3100"

[[phoneNumbers]]  # list
type = "home"
number = "212 555-1234"

[[phoneNumbers]]
type = "office"
number = "646 555-4567"

[newsection.under_another]  # indentation not required
pew = 2
```
