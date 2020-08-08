-- citi name with
-- state name
SELECT cities.id, cities.name, states.name
FROM hbtn.states, hbtn.cities
WHERE hbtn.cities.state_id = hbtn.states.id
ORDER BY hbtn.cities.id;
