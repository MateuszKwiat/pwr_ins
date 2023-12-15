-- 1


-- 2
select count(doc->'geography'->>'Continent'), doc->'geography'->>'Continent'
from countryinfo
group by doc->'geography'->>'Continent'
order by count(doc->'geography'->>'Continent') desc
limit 1


-- 3


-- 4


-- 5


-- 6


