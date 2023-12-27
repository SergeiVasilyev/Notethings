/**
 * @license Copyright (c) 2003-2023, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	config.language = 'en';
	config.uiColor = '#ffeee1';
	// config.height = '100%';
	config.autoGrow_onStartup = true;
	config.toolbar = [
		{
			name: 'various',
			items: ['Source', '-', 'Bold', 'Italic', 'ExportPdf',]
		},

	];
	config.extraPlugins = "exportpdf, div, autolink, autoembed, embedsemantic, autogrow, devtools, widget, lineutils, clipboard, dialog, dialogui, elementspath, codesnippet";
};
