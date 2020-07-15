-- nested queries
-- get information from another table
SELECT id, state_id, name FROM hbtn_0d_usa.cities WHERE states_id = (
  SELECT id FROM hbtn_0d_usa.states
  WHERE name = 'California'
)ORDER BY cities.id;
