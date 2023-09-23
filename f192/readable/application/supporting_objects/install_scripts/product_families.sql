create table eba_cust_product_families (
    id                  number       not null,
    row_version_number  number,
    name                varchar2(60) not null,
    description         varchar2(4000),
    --
    created             timestamp with time zone not null,
    created_by          varchar2(255) not null,
    updated             timestamp with time zone,
    updated_by          varchar2(255),
    --
    constraint eba_cust_prod_families_pk primary key (id)
)
/
create unique index eba_cust_prod_families_uk on eba_cust_product_families(name)
/

create or replace trigger biu_eba_cust_product_families
    before insert or update on eba_cust_product_families
    for each row
begin
    if inserting then
        if :new.id is null then
            :new.id := to_number(sys_guid(),'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX');
        end if;
        :new.created := current_timestamp;
        :new.created_by := nvl(v('APP_USER'),user);
        :new.row_version_number := 1;
    else
        :new.row_version_number := nvl(:new.row_version_number,0) + 1;
    end if;
    :new.updated := current_timestamp;
    :new.updated_by := nvl(v('APP_USER'),user);
end biu_eba_cust_product_families;
/
alter trigger biu_eba_cust_product_families enable;
/
