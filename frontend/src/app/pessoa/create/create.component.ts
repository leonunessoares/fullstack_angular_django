import { Component, OnInit } from '@angular/core';
import { PessoaService } from '../pessoa.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {
  
  form: FormGroup ;

  constructor(
    private fb: FormBuilder,
    public pessoaService: PessoaService,
    private router: Router
  ) { }

  ngOnInit(): void {

    this.form = this.fb.group({
      id: [''],
      nome: ['', Validators.required],
      data_nasc: ['', Validators.required],
      cpf: ['', [Validators.required, Validators.pattern(/^\d{11}$/)]],
      sexo: ['', Validators.required],
      altura: ['', [Validators.required, Validators.min(0.5)]],
      peso: ['', [Validators.required, Validators.min(0.1)]]
    });

  }

  get f(){
    return this.form.controls;
  }

  submit(){
    console.log(this.form.value);
    this.pessoaService.addPessoa(this.form.value).subscribe(res => {
         console.log('Pessoa criada com sucesso!');
         this.router.navigateByUrl('pessoa/index');
    })
  }

}


