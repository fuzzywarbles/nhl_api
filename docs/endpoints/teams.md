# Teams

##### Endpoint URL
>[https://statsapi.web.nhl.com/api/v1/teams](https://statsapi.web.nhl.com/api/v1/teams)
<br/><br/>
>[https://statsapi.web.nhl.com/api/v1/teams/ID](https://statsapi.web.nhl.com/api/v1/teams/ID)

##### Valid URL
>[https://statsapi.web.nhl.com/api/v1/teams](https://statsapi.web.nhl.com/api/v1/teams)
<br/><br/>
>[https://statsapi.web.nhl.com/api/v1/teams/1](https://statsapi.web.nhl.com/api/v1/teams/1)

## Modifiers
`?expand=team.roster` - Shows roster of active players for the specified team 

`?expand=team.schedule.next` - Returns details of the upcoming game for a team

`?expand=team.schedule.previous` - Same as above but for the last game played

`?expand=team.stats` - Returns the teams stats for the season

##### Valid URL w/ modifiers
>[https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster&expand=team.schedule.next&expand=team.schedule.previous&expand=team.stats](https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster&expand=team.schedule.next&expand=team.schedule.previous&expand=team.stats)
<br/><br/>
>[https://statsapi.web.nhl.com/api/v1/teams/1?expand=team.roster&expand=person.names&expand=team.schedule.next&expand=team.schedule.previous&expand=team.stats](https://statsapi.web.nhl.com/api/v1/teams/1?expand=team.roster&expand=person.names&expand=team.schedule.next&expand=team.schedule.previous&expand=team.stats)

## Data Sets
#### Teams `teams`
```text
["id", "name", "link", "venue_id", "venue_name", "venue_link", "venue_city", "timeZone_id", "timeZone_offset", "timeZone_tz", "abbreviation", "teamName", "locationName", "firstYearOfPlay" , "division_id", "division_name", "division_nameShort", "division_link", "division_abbreviation", "conference_id", "conference_name", "conference_link", "franchise_id", "franchise_teamName", "franchise_link", "shortName", "officialSiteUrl", "franchiseId", "active"]
```

## RETURNED JSON
```json
{
    "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
    "teams" : [ {
        "id" : 1,
        "name" : "New Jersey Devils",
        "link" : "/api/v1/teams/1",
        "venue" : {
            "id" : 5067,
            "name" : "Prudential Center",
            "link" : "/api/v1/venues/5067",
            "city" : "Newark",
            "timeZone" : {
                "id" : "America/New_York",
                "offset" : -4,
                "tz" : "EDT"
            }
        },
        "abbreviation" : "NJD",
        "teamName" : "Devils",
        "locationName" : "New Jersey",
        "firstYearOfPlay" : "1982",
        "division" : {
            "id" : 18,
            "name" : "Metropolitan",
            "nameShort" : "Metro",
            "link" : "/api/v1/divisions/18",
            "abbreviation" : "M"
        },
        "conference" : {
            "id" : 6,
            "name" : "Eastern",
            "link" : "/api/v1/conferences/6"
        },
        "franchise" : {
            "franchiseId" : 23,
            "teamName" : "Devils",
            "link" : "/api/v1/franchises/23"
        },
        "shortName" : "New Jersey",
        "officialSiteUrl" : "http://www.newjerseydevils.com",
        "franchiseId" : 23,
        "active" : true
    } ]
}
```

## MODIFIED JSON
```json
{   
    "data_sets": {
        "teams" : [
            "id",
            "name",
            "link",
            "venue_id",
            "venue_name",
            "venue_link",
            "venue_city",
            "timeZone_id",
            "timeZone_offset",
            "timeZone_tz",
            "abbreviation",
            "teamName",
            "locationName",
            "firstYearOfPlay" ,
            "division_id",
            "division_name",
            "division_nameShort",
            "division_link",
            "division_abbreviation",
            "conference_id",
            "conference_name",
            "conference_link",
            "franchise_id",
            "franchise_teamName",
            "franchise_link",
            "shortName",
            "officialSiteUrl",
            "franchiseId",
            "active"
        ]
    }
}
```
