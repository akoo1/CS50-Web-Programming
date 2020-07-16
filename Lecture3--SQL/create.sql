

CREATE TABLE flights (

  /* The data and data type that will be stored in each column in a table.
     The thrid column in here is some other optional constrains. */
  id SERIAL PRIMARY KEY,          /* each flight will have an automatically incrementing integer as its id */
  origin VARCHAR NOT NULL,        /* we will represent the flight's origin by text */
  destination VARCHAR NOT NULL,
  duaration INTEGER NOT NULL

);
