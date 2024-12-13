    CrEaTe    TaBlE    Customers   (
   CustomerId    INT     PRIMARY KEY,
CustomerName  VaRcHaR(255)    NOT NULL ,
   created_at   datetime  DEFAULT CURRENT_TIMESTAMP,
   Address  VARCHAR(255),
City  VARCHAR(50)  ,
  Country   VARCHAR(50)
   );
  Insert    INTO   Customers( CustomerId,CustomerName,   Address,City,Country)
values  (1,'John Doe','123 Apple St','New York','USA');
insert into Customers(CustomerId, CustomerName,Address,City,Country)
values
 (2,'Jane Smith','456 Orange Av','Los Angeles','USA'),
 (3,'Mario Rossi','Via Roma 10','Rome','Italy'),
      (4,'Réne Dupont','12 Rue Lafayette','Paris','France') ;
Select   CustomerId  ,    CustomerName,
Address , City,   Country,   created_at
   fRoM Customers
where Country='USA' Or Country='Italy'
  ORDER   By      created_at   DESC ;
   UpDatE  Customers
    sEt Address='789 Cherry Rd', City='Chicago',Country='USA'
   wHeRe    CustomerId=1   ;
Delete   from Customers
   where  CustomerId=3;
    CrEaTe TaBlE  Orders(
orderid   int primary key,
   CustomerID int not null,
OrderDate datetime default current_timestamp,
Amount decimal(10,2) not null
);
Insert into   Orders(orderid, customerid, amount)
values (101,1,99.95),(102,2,150.00);
Select    c.CustomerName,
   o.orderid,   o.amount, o.orderdate
   FROM
   customers c
  JOIN   orders o
    on c.customerid=o.customerid
   where  c.country='usa'
   order    by  c.customername  Asc,
       o.amount desc  ;


-- some comments to test formatting
-- another comment line
