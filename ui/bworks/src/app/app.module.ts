import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

//import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';

import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RegisterComponent } from './components/register/register.component';
import { TransactionComponent } from './components/transaction/transaction.component';


import { AppRoutingModule } from './app-routing.module';
import { StartAppComponent } from './components/start-app/start-app.component';
import { EtlTransactionsComponent } from './components/etl-transactions/etl-transactions.component';
import { ConfigureDataComponent } from './components/configure-data/configure-data.component';

import { AgGridModule } from 'ag-grid-angular';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    TransactionComponent,
    StartAppComponent,
    EtlTransactionsComponent,
    ConfigureDataComponent
    
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    AgGridModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
