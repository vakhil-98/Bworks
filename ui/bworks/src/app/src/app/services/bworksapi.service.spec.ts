import { TestBed } from '@angular/core/testing';

import { BworksapiService } from './bworksapi.service';

describe('BworksapiService', () => {
  let service: BworksapiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BworksapiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
