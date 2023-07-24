import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';



@Component({
  selector: 'app-start-app',
  templateUrl: './start-app.component.html',
  styleUrls: ['./start-app.component.css']
})

export class StartAppComponent implements OnInit{
  

  constructor(private router: Router) { }
  ngOnInit(): void {
    // Initialization tasks go here
   

      
   // this.router.navigate(['/']);


  }

}
