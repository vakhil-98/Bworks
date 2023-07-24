import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfigureDataComponent } from './configure-data.component';

describe('ConfigureDataComponent', () => {
  let component: ConfigureDataComponent;
  let fixture: ComponentFixture<ConfigureDataComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ConfigureDataComponent]
    });
    fixture = TestBed.createComponent(ConfigureDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
