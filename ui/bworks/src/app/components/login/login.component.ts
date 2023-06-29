import { Component, OnInit, OnDestroy } from '@angular/core';
import { BworksapiService } from 'src/app/services/bworksapi.service';
import { User, LoginRequest } from 'src/app/datamodels/bworksmodel';
import { Subscription } from 'rxjs';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit, OnDestroy {
  email: string = "";
  password: string = "";
  enable_Register: boolean = false;
  subscription: Subscription | undefined;
  transaction_enable : boolean = false;

  constructor(private bworksApi: BworksapiService, private userService: UserService) { }

  ngOnInit(): void {
    // Initialization tasks go here
    console.log('Component initialized');
    this.subscription = this.userService.getRegistrationStatus().subscribe(status => {
      this.enable_Register = status;
    });
  }

 register(){
  this.userService.setRegistrationStatus(true);
 }

  login() {
    let data: LoginRequest = {
      UserName: this.email,
      Password: this.password
    };

    this.bworksApi.login(data).subscribe((resp: User) => {
      console.log(resp.ContactId);

    if(resp!= undefined && resp != null){
      this.userService.setuserId(resp.UserId);
      this.transaction_enable = true

      
    }
    });
  }

  showConfigResponse() {
    // Code for showing config response goes here
  }

  ngOnDestroy(): void {
    // Cleanup tasks go here
    console.log('Component destroyed');
    this.subscription?.unsubscribe();
    
  }
}

