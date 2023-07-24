import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { TransactionComponent } from './components/transaction/transaction.component';
import { EtlTransactionsComponent } from './components/etl-transactions/etl-transactions.component';
import { ConfigureDataComponent } from './components/configure-data/configure-data.component';

const routes: Routes = [ 

  {
    path: '**',   redirectTo: 'configuredata', pathMatch: 'full'
  },

  {
    path:"login", component:LoginComponent
  },

  {
    path:"register", component:RegisterComponent
  },

  {
    path:"transaction", component:TransactionComponent
  },

  // { 
  //   path: '**',   redirectTo: '/login', pathMatch: 'full' 
  // },
  
  {
    path:"etlbicycles", component:EtlTransactionsComponent
  },

  {
    path:"configuredata", component:ConfigureDataComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
