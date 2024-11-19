create database karan;
use karan;
create table asset(date date,asset_id int auto_increment,asset_name varchar(255),asset_type varchar(255),asset_value decimal(10,2));
create table liability(date date,liab_id int auto_increment,liab_name varchar(255),liab_type varchar(255),liab_value decimal(10,2));