import { Component, OnInit } from '@angular/core';
import { EtlTransactions } from 'src/app/datamodels/bworksmodel';
import { BworksapiService } from 'src/app/services/bworksapi.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-etl-transactions',
  templateUrl: './etl-transactions.component.html',
  styleUrls: ['./etl-transactions.component.css']
})
export class EtlTransactionsComponent implements OnInit {

  etl_bicycle_data: EtlTransactions = {
    status : false,
    records_inserted : 0
  };


constructor(private bworksApi:BworksapiService, private userService: UserService){ }
ngOnInit(): void {
     this.userService.setRegistrationStatus(false);
  }
etl_bicycles() {

    this.bworksApi.etl_bicycles().subscribe((resp: EtlTransactions) => {
      console.log(resp.records_inserted,resp.status);
  
    if(resp!= undefined && resp != null){
      this.etl_bicycle_data = resp;
  
    }

    });
  }


}

