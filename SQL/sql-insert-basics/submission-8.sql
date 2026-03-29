CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');
CREATE SEQUENCE noid_test START WITH 1000 INCREMENT BY 1000 NO MAXVALUE;

CREATE TABLE bank_accounts (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    account_type account_type,
    balance INTEGER DEFAULT nextval('noid_test'),
    PRIMARY KEY (id)
);
-- Do not modify above this line --


INSERT INTO bank_accounts (account_type)
VALUES ('checking'),
    ('savings'),
    ('cd'),
    ('money_market');








-- Do not modify below this line --
SELECT * FROM bank_accounts;
