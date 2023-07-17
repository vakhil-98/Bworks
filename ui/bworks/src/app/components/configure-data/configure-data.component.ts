import { Component } from '@angular/core';
import { AgGridAngular } from 'ag-grid-angular';
import { CellClickedEvent, ColDef, GridReadyEvent } from 'ag-grid-community';

@Component({
  selector: 'app-configure-data',
  templateUrl: './configure-data.component.html',
  styleUrls: ['./configure-data.component.css']
})
export class ConfigureDataComponent {

  public columnDefs: ColDef[] = [
    {
      headerName: "Name",
      field: "Name",
      headerTooltip: "Full name(s) of donor",
    },

    {
      headerName: "EmailId",
      field: "EmailId",
      headerTooltip: "Email address",
    },

    {
      headerName: "Survey",
      field: "Survey",
      headerTooltip: "How did you hear about us?",
    },

    {
      headerName: "DropOff_Location",
      field: "DropOff_Location",
      headerTooltip: "drop off location",
    },

    {
      headerName: "Bike(s) Model",
      field: "BikeModel",
      headerTooltip: "Bike's Model",
    },

    {
      headerName: "Bike(s) Color",
      field: "BikeColor",
      headerTooltip: "Bike(s) Color",
    },

    {
      headerName: "Bike(s) Wheel Size",
      field: "BikeWheel",
      headerTooltip: "Bike(s) Wheel Size",
    },

    {
      headerName: "Donated_On",
      field: "DateTime",
      headerTooltip: "donated_on",
    },
]

public rowData: any[]= []
public onGridReady(event:any) {
  this.rowData = [
    {
      Name : "Naga",
      EmailId: "abc@gmail.com",
      Survey: "Friends",
      DropOff_Location:"Wgl",
      BikeModel:"Atlas",
      BikeColor:"Blue",
      BikeWheel:"20",
      DateTime: "14-11-2023"
    }
  ]
}

 }