import { Component } from '@angular/core';
import { Bicycle, Transaction } from 'src/app/datamodels/bworksmodel';
import { BworksapiService } from 'src/app/services/bworksapi.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.css']
})


export class TransactionComponent {

  dateofdonate: String = ""
  bicycleId: Number = 0
  address:String = ""
  contact:Number = 0
  donatebuy:String = ""
  bicycles:Bicycle[] = []
  userId:Number = 0
 
  constructor(private bworksApi :BworksapiService, private userService: UserService){}
  // bicycles:any[] = [
  //   {id : 1,name : "cycle1"},
  //   {id : 2,name : "cycle2"},
  //   {id : 3,name : "cycle3"},
  // ]

  ngOnInit(): void {
   this.getBicycle();
   this.userService.getuserId().subscribe(id => {
    this.userId = id;
  });
  }

  Create(){
    console.log(this.bicycleId)

  }
  selectedbicycles(event:any){
    this.bicycleId = event.target.value
    console.log(this.bicycleId)
  }

  donate_buy(event:any){
    this.donatebuy = event.target.value
    console.log(this.donatebuy)
  }


  getBicycle() {

    this.bworksApi.getBicycles().subscribe((resp: Bicycle[]) => {
      console.log(resp[0].cycleName);

    if(resp!= undefined && resp != null){
      this.bicycles = resp;

    }
    });
  }
  Submit() {
    let data: Transaction = {
      UserId: this.userId,
      BicycleId: this.bicycleId,
      BicycleNo: 33,
      IsBuy: (this.donatebuy=="buy")?true:false,
      IsDonate: (this.donatebuy=="donate")?true:false,
      Address: this.address,
      ContactId: this.contact,
      // DateOfDonate:String
      // DateOfBuy:String
    };

    this.bworksApi.transaction(data).subscribe((resp: any) => {
      

    if(resp!= undefined && resp != null){
      console.log(resp["issuccess"])
      

    }
    });
  }

}
