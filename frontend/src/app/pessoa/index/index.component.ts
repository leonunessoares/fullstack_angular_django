import { Component,OnInit } from '@angular/core';
import { PessoaService } from '../pessoa.service';
import { Pessoa } from '../pessoa';
import { ActivatedRoute, Router } from '@angular/router';
import { ModalComponent } from '../../modal/modal.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent  implements OnInit  {
  pessoas: Pessoa[] = [];

  // constructor() { }
  constructor(public pessoaService: PessoaService,private router: Router,private modalService: NgbModal) { }

  ngOnInit(): void {
    this.pessoaService.getPessoas().subscribe((data: Pessoa[])=>{
      this.pessoas = data;
      console.log(this.pessoas);
    })
  }

  deletePessoa(id: number){
    this.pessoaService.deletePessoa(id).subscribe(res => {
         this.pessoas = this.pessoas.filter(item => item.id !== id);
         console.log('Pessoa excluída com sucesso!');
    })
  }
  verPeso(altura: number , sexo:string){   
    this.pessoaService.calcularPesoIdeal(altura, sexo).subscribe(data => {
      this.openModal(data.peso_ideal.toFixed(2));
    });
  }

  openModal(pesoIdeal: number): void {
    const modalRef = this.modalService.open(ModalComponent);
    modalRef.componentInstance.pesoIdeal = pesoIdeal;
  }
}
