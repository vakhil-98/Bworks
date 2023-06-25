import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { UserService } from 'src/app/services/user.service';
import { BworksapiService } from 'src/app/services/bworksapi.service';
import { RegisterUser, User } from 'src/app/datamodels/bworksmodel';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})

export class RegisterComponent implements OnInit {
enable_Register:boolean = true;
email:String = ""
username:String = ""
password:String = ""
contact:Number = 0
address:String = ""
name:String = ""

subscription: Subscription | undefined;

constructor(private bworksApi: BworksapiService, private userService: UserService) { }
ngOnInit(): void {
  // Initialization tasks go here
  console.log('Component initialized');
  // this.subscription = this.userService.getRegistrationStatus().subscribe(status => {
  // this.enable_Register = status;
  // })
  this.userService.setRegistrationStatus(true)
}


Signup(){

  this.userService.setRegistrationStatus(false)
  let user:RegisterUser = {
    UserName : this.username,
    Password : this.password,
    Address : this.address,
    Email : this.email,
    ContactId : this.contact,
    Name: this.name

  }
  this.bworksApi.register(user).subscribe((resp) => {
  console.log(resp);
  });
}
cancel(){

  this.userService.setRegistrationStatus(false)
}

}
