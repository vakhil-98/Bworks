import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  
  private registrationStatusSubject: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  private userId: BehaviorSubject<Number> = new BehaviorSubject<Number>(0);

  constructor() { }

  setRegistrationStatus(status: boolean): void {
    this.registrationStatusSubject.next(status);
  }

  getRegistrationStatus(): BehaviorSubject<boolean> {
    return this.registrationStatusSubject;
  }

  setuserId(id: Number): void {
    this.userId.next(id);
  }

  getuserId(): BehaviorSubject<Number> {
    return this.userId;
  }
}
