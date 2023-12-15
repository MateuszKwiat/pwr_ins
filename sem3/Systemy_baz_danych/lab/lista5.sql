-- 1
select distinct on (doc->'government'->>'GovernmentForm') 
doc->'government'->>'GovernmentForm'
from countryinfo

-- 2
select count(doc->'geography'->>'Continent'), doc->'geography'->>'Continent'
from countryinfo
group by doc->'geography'->>'Continent'
order by count(doc->'geography'->>'Continent') desc
limit 1

-- 3
select doc->>'Name', doc->>'IndepYear' 
from countryinfo
where doc->>'IndepYear' != 'null'
order by cast(doc->>'IndepYear' as integer) desc

-- 4
select Language, count(Language) filter (where IsOfficial = 'T')
from countryLanguage
group by Language
order by count(Language) desc

-- 5


-- 6
select doc->>'Name', doc->>'GNP', doc->'demographics'->>'LifeExpectancy'
from countryinfo
where doc->>'GNP' != '0' anddoc->'demographics'->>'LifeExpectancy' != 'null'
order by cast(doc->>'GNP' as float) desc,
cast(doc->'demographics'->>'LifeExpectancy' as float) desc
limit 20

