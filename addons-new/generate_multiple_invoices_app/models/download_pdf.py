# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import base64
from zipfile import ZIP_DEFLATED, ZipFile
import io
import os

class WizardMultipleInv(models.TransientModel):
	_name = 'wizard.download.pdf'
	_description='Download PDF'

	pdf_report = fields.Selection([('invoice','Invoice'),
			('inv_payment','Invoice Without Payment'),
			('recurring','Recurring Invoice'),
			('prepayment','Prepayment Invoice'),
			('final','Final Bill/Invoice'),
			('sales','Sales Invoice')],
			'PDF Report',required=True)
	state = fields.Selection([('draft','Draft'),
			('done','Done')],
			'Stage',default= 'draft')
	download_pdf_report = fields.Binary('Download PDF Report',
		readonly=True)
	file_name = fields.Char(string='Name')


	def wizard_binary(self):
		list1 = []
		if self.pdf_report == 'recurring':
			var = 0
			for active_ids in self.env['account.move'].browse(self._context.get('active_ids')):
				pdf = self.env.ref('browseinfo_rental_management.action_invoice_recurring')._render_qweb_pdf(active_ids.id)[0]
				list1.append(active_ids)
				active_ids.name = active_ids.name +" - "+ active_ids.partner_id.lastname + " - " +  active_ids.partner_id.firstname
				#raise UserError(str(self.env['account.move'].browse(self._context.get('active_ids'))))
				
				if active_ids.name == '/':
					var += 1
					with open('/tmp/' +(active_ids.name).replace('/','_') + "%s.pdf" % (var), "wb") as outfile:
						outfile.write(pdf)
				else:
					with open('/tmp/' +(active_ids.name).replace('/','_') + ".pdf", "wb") as outfile:
						outfile.write(pdf)

			dir_path = os.path.dirname(os.path.realpath(__file__))
			full_path = dir_path + '/allpdffiles.zip'
			zipf = ZipFile(full_path, 'w', ZIP_DEFLATED)
			with zipf as myzip:
				var2 = 0
				for order in list1:
					if order.name == '/':
						var2 += 1
						myzip.write('/tmp/' +(order.name).replace('/','_') + "%s.pdf" % (var2))
					else:
						myzip.write('/tmp/' +(order.name).replace('/','_') + ".pdf")
			
			with open(full_path, "rb") as f:
				converts = f.read()
				encoded = base64.b64encode(converts)

			self.file_name = 'Invoices.zip'	
			self.download_pdf_report = encoded

			var3 = 0
			for result in list1:
				if result.name == '/':
					var3 += 1
					os.remove('/tmp/' +(result.name).replace('/','_') + "%s.pdf" % (var3))
				else:
					os.remove('/tmp/' +(result.name).replace('/','_') + ".pdf")

		if self.pdf_report == 'sales':
			var = 0
			for active_ids in self.env['account.move'].browse(self._context.get('active_ids')):
				pdf = self.env.ref('browseinfo_rental_management.action_sales_invoice')._render_qweb_pdf(active_ids.id)[0]
				list1.append(active_ids)
				active_ids.name = active_ids.name +" - "+ active_ids.partner_id.lastname + " - " +  active_ids.partner_id.firstname
				
				if active_ids.name == '/':
					var += 1
					with open('/tmp/' +(active_ids.name).replace('/','_') + "%s.pdf" % (var), "wb") as outfile:
						outfile.write(pdf)
				else:
					with open('/tmp/' +(active_ids.name).replace('/','_') + ".pdf", "wb") as outfile:
						outfile.write(pdf)

			dir_path = os.path.dirname(os.path.realpath(__file__))
			full_path = dir_path + '/allpdffiles.zip'
			zipf = ZipFile(full_path, 'w', ZIP_DEFLATED)
			with zipf as myzip:
				var2 = 0
				for order in list1:
					if order.name == '/':
						var2 += 1
						myzip.write('/tmp/' +(order.name).replace('/','_') + "%s.pdf" % (var2))
					else:
						myzip.write('/tmp/' +(order.name).replace('/','_') + ".pdf")
			
			with open(full_path, "rb") as f:
				converts = f.read()
				encoded = base64.b64encode(converts)

			self.file_name = 'Invoices.zip'	
			self.download_pdf_report = encoded

			var3 = 0
			for result in list1:
				if result.name == '/':
					var3 += 1
					os.remove('/tmp/' +(result.name).replace('/','_') + "%s.pdf" % (var3))
				else:
					os.remove('/tmp/' +(result.name).replace('/','_') + ".pdf")

		if self.pdf_report == 'prepayment':
			var = 0
			for active_ids in self.env['account.move'].browse(self._context.get('active_ids')):
				pdf = self.env.ref('browseinfo_rental_management.action_invoice_prepayment')._render_qweb_pdf(active_ids.id)[0]
				list1.append(active_ids)
				active_ids.name = active_ids.name +" - "+ active_ids.partner_id.lastname + " - " +  active_ids.partner_id.firstname
				
				if active_ids.name == '/':
					var += 1
					with open('/tmp/' +(active_ids.name).replace('/','_') + "%s.pdf" % (var), "wb") as outfile:
						outfile.write(pdf)
				else:
					with open('/tmp/' +(active_ids.name).replace('/','_') + ".pdf", "wb") as outfile:
						outfile.write(pdf)

			dir_path = os.path.dirname(os.path.realpath(__file__))
			full_path = dir_path + '/allpdffiles.zip'
			zipf = ZipFile(full_path, 'w', ZIP_DEFLATED)
			with zipf as myzip:
				var2 = 0
				for order in list1:
					if order.name == '/':
						var2 += 1
						myzip.write('/tmp/' +(order.name).replace('/','_') + "%s.pdf" % (var2))
					else:
						myzip.write('/tmp/' +(order.name).replace('/','_') + ".pdf")
			
			with open(full_path, "rb") as f:
				converts = f.read()
				encoded = base64.b64encode(converts)

			self.file_name = 'Invoices.zip'	
			self.download_pdf_report = encoded

			var3 = 0
			for result in list1:
				if result.name == '/':
					var3 += 1
					os.remove('/tmp/' +(result.name).replace('/','_') + "%s.pdf" % (var3))
				else:
					os.remove('/tmp/' +(result.name).replace('/','_') + ".pdf")

		if self.pdf_report == 'final':
			var = 0
			for active_ids in self.env['account.move'].browse(self._context.get('active_ids')):
				pdf = self.env.ref('browseinfo_rental_management.action_report_rental_invoice')._render_qweb_pdf(active_ids.id)[0]
				list1.append(active_ids)
				active_ids.name = active_ids.name +" - "+ active_ids.partner_id.lastname + " - " +  active_ids.partner_id.firstname
				
				if active_ids.name == '/':
					var += 1
					with open('/tmp/' +(active_ids.name).replace('/','_') + "%s.pdf" % (var), "wb") as outfile:
						outfile.write(pdf)
				else:
					with open('/tmp/' +(active_ids.name).replace('/','_') + ".pdf", "wb") as outfile:
						outfile.write(pdf)

			dir_path = os.path.dirname(os.path.realpath(__file__))
			full_path = dir_path + '/allpdffiles.zip'
			zipf = ZipFile(full_path, 'w', ZIP_DEFLATED)
			with zipf as myzip:
				var2 = 0
				for order in list1:
					if order.name == '/':
						var2 += 1
						myzip.write('/tmp/' +(order.name).replace('/','_') + "%s.pdf" % (var2))
					else:
						myzip.write('/tmp/' +(order.name).replace('/','_') + ".pdf")
			
			with open(full_path, "rb") as f:
				converts = f.read()
				encoded = base64.b64encode(converts)

			self.file_name = 'Invoices.zip'	
			self.download_pdf_report = encoded

			var3 = 0
			for result in list1:
				if result.name == '/':
					var3 += 1
					os.remove('/tmp/' +(result.name).replace('/','_') + "%s.pdf" % (var3))
				else:
					os.remove('/tmp/' +(result.name).replace('/','_') + ".pdf")

		if self.pdf_report == 'inv_payment':
			var = 0
			for active_ids in self.env['account.move'].browse(self._context.get('active_ids')):
				pdf = self.env.ref('account.account_invoices')._render_qweb_pdf(active_ids.id)[0]
				list1.append(active_ids)
				active_ids.name = active_ids.name +" - "+ active_ids.partner_id.lastname + " - " +  active_ids.partner_id.firstname
				
				if active_ids.name == '/':
					var += 1
					with open('/tmp/' +(active_ids.name).replace('/','_') + "%s.pdf" % (var), "wb") as outfile:
						outfile.write(pdf)
				else:
					with open('/tmp/' +(active_ids.name).replace('/','_') + ".pdf", "wb") as outfile:
						outfile.write(pdf)

			dir_path = os.path.dirname(os.path.realpath(__file__))
			full_path = dir_path + '/allpdffiles.zip'
			zipf = ZipFile(full_path, 'w', ZIP_DEFLATED)
			with zipf as myzip:
				var2 = 0
				for order in list1:
					if order.name == '/':
						var2 += 1
						myzip.write('/tmp/' +(order.name).replace('/','_') + "%s.pdf" % (var2))
					else:
						myzip.write('/tmp/' +(order.name).replace('/','_') + ".pdf")
			
			with open(full_path, "rb") as f:
				converts = f.read()
				encoded = base64.b64encode(converts)

			self.file_name = 'Invoices Without Payment.zip'	
			self.download_pdf_report = encoded

			var3 = 0
			for result in list1:
				if result.name == '/':
					var3 += 1
					os.remove('/tmp/' +(result.name).replace('/','_') + "%s.pdf" % (var3))
				else:
					os.remove('/tmp/' +(result.name).replace('/','_') + ".pdf")

		elif self.pdf_report == 'invoice':
			var = 0
			for active_ids in self.env['account.move'].browse(self._context.get('active_ids')):
				pdf = self.env.ref('account.account_invoices')._render_qweb_pdf(active_ids.id)[0]
				list1.append(active_ids)
				if active_ids.name == '/':
					var += 1
					with open('/tmp/' +(active_ids.name).replace('/','_') + "%s.pdf" % (var), "wb") as outfile:
						outfile.write(pdf)
				else:
					with open('/tmp/' +(active_ids.name).replace('/','_') + ".pdf", "wb") as outfile:
						outfile.write(pdf)

			dir_path = os.path.dirname(os.path.realpath(__file__))
			full_path = dir_path + '/allpdffiles.zip'
			zipf = ZipFile(full_path, 'w', ZIP_DEFLATED)
			with zipf as myzip:
				var2 = 0
				for order in list1:
					if order.name == '/':
						var2 += 1
						myzip.write('/tmp/' +(order.name).replace('/','_') + "%s.pdf" % (var2))
					else:
						myzip.write('/tmp/' +(order.name).replace('/','_') + ".pdf")

			with open(full_path, "rb") as f:
				converts = f.read()
				encoded = base64.b64encode(converts)

			self.file_name = 'Invoices.zip'	
			self.download_pdf_report = encoded

			var3 = 0
			for result in list1:
				if result.name == '/':
					var3 += 1
					os.remove('/tmp/' +(result.name).replace('/','_') + "%s.pdf" % (var3))
				else:
					os.remove('/tmp/' +(result.name).replace('/','_') + ".pdf")

		self.write({'state':'done'})

		for inv in self.env['account.move'].browse(self._context.get('active_ids')):
			inv.name = inv.payment_reference

		return {
			'name':'Download Multiple Separate Invoices',
			'type': 'ir.actions.act_window',
			'view_mode': 'form',
			'res_model': 'wizard.download.pdf',
			'res_id': self.id,
			'target': 'new',
		}


	def wizard_download(self):
		return {'type': 'ir.actions.act_window_close'}
