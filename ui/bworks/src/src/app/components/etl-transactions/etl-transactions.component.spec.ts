import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EtlTransactionsComponent } from './etl-transactions.component';

describe('EtlTransactionsComponent', () => {
  let component: EtlTransactionsComponent;
  let fixture: ComponentFixture<EtlTransactionsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EtlTransactionsComponent]
    });
    fixture = TestBed.createComponent(EtlTransactionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
