-- nested queries
-- get information from another table
SELECT * FROM hbtn_0d_usa.cities WHERE states_id = (
  SELECT id FROM hbtn_0d_usa.states
  WHERE name = CAalifornia
);
