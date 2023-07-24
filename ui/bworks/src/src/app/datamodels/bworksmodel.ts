export interface User {
    Address: String,
    ContactId: Number,
    Email: String,
    Name: String,
    UserId: Number,
    UserName: String,
    Password: String

}

export interface LoginRequest {
   
    UserName: String,
    Password: String
}

export interface Bicycle {
   
    bicycleId: Number,
    cycleImage: String
    cycleName: String
}

export interface Transaction {
   
   
    UserId: Number
    BicycleId: Number,
    BicycleNo: Number,
    IsBuy: Boolean,
    IsDonate: Boolean,
    Address: String,
    ContactId: Number,
    // DateOfDonate:String
    // DateOfBuy:String

}

export interface RegisterUser {
    Address: String,
    ContactId: Number,
    Email: String,
    Name: String,
    UserName: String,
    Password: String

}

export interface EtlTransactions{
    status:boolean,
    records_inserted:Number 
}