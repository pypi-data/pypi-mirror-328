import itertools
import sys

from pnb.mcl.io.xmi import read_xmi
import rdflib
from rdflib import Literal, RDF, BNode


class RdfExporter:

    def __init__(self, model, metamodel_namespace = 'http://www.plants-and-bytes.de/mcl/meta/'):
        
        self.model = model
        
        self.meta_model = sys.modules[model.__module__]
        self.graph = rdflib.Graph()
        self.node_by_element = {}
        self.meta_model_namespace = rdflib.Namespace(metamodel_namespace)
        self.graph.bind('meta', self.meta_model_namespace)
        self.add_element(model)

        
    def get_element_node(self, element):
        
        assert isinstance(element, self.meta_model.Element), element
        
        node = self.node_by_element.get(element)
        if node is None:
            if isinstance(element, self.meta_model.Model):
                if element.uri is None:
                    assert element.name == 'builtin'
                    uri = 'http://www.plants-and-bytes.de/mcl/builtin'
                else:
                    uri = element.uri
                node = rdflib.URIRef(uri)
                self.graph.bind(element.name, node+'/')
            elif isinstance(element, self.meta_model.Object):
                name = element.name
                if name:
                    node = rdflib.URIRef(self.get_element_node(element.model) + '/' + name) # TODO: check unique
                else:
                    model = element.model
                    assert model is self.model
                    node = BNode()
            else:
                owner = element.owner
                owner_node = self.get_element_node(owner)
                if isinstance(owner, self.meta_model.Model):
                    intro = owner_node + '/'
                else:
                    intro = owner_node + '.'
                node = rdflib.URIRef(intro + element.name)

            
            self.node_by_element[element] = node
            
        return node
            
            
            
        


    def add(self, s, p, o):
        triple = s, p, o
        if None not in triple:
            self.graph.add(triple)
            
            
    def extend(self, node, values, property_):
        
        for value in values:
            assert isinstance(value, rdflib.Node)
            self.add(node, property_, value)
            
            
    def extend_with_list(self, node, elements, property_):
        self.extend(node, elements, property_) # TODO
        
        
    def add_element(self, element):
        
        assert isinstance(element, self.meta_model.Element), element

        node = self.get_element_node(element)
        self.add(node, RDF.type, self.meta_model_namespace.term(element.get_meta_class_name()))

        if isinstance(element, self.meta_model.NamedElement):
            if element.name:
                self.add(node, self.meta_model_namespace.name, Literal(element.name))

        if isinstance(element, self.meta_model.Package):
            self.extend(node, [self.add_element(pe) for pe in element.packagedElements], self.meta_model_namespace.packagedElement)

        if isinstance(element, self.meta_model.Type):
            self.extend(node, [self.get_element_node(st) for st in element.superTypes], self.meta_model_namespace.superType)
            self.extend(node, [self.add_element(at) for at in element.ownedAttributes], self.meta_model_namespace.ownedAttribute)

        if isinstance(element, self.meta_model.Property):
            self.add(node, self.meta_model_namespace.type, self.get_element_node(element.type))
            self.add(node, self.meta_model_namespace.term('lower'), Literal(element.lower))
            if element.upper is not None:
                self.add(node, self.meta_model_namespace.term('upper'), Literal(element.upper))
            self.add(node, self.meta_model_namespace.isOrdered, Literal(element.isOrdered))
            if isinstance(
                    element, (self.meta_model.ReferenceProperty, self.meta_model.DataProperty)):
                self.add(node, self.meta_model_namespace.isUnique, Literal(element.isUnique))
            if isinstance(element, self.meta_model.ReferenceProperty):
                self.add(node, self.meta_model_namespace.term('oppositeLower'),
                    Literal(element.oppositeLower))
                if element.oppositeUpper is not None:
                    self.add(node, self.meta_model_namespace.term('oppositeUpper'),
                        Literal(element.oppositeUpper))

        if isinstance(element, self.meta_model.Enumeration):
            TODO
            add_children(item.orderedOwnedLiterals)


        if isinstance(element, self.meta_model.Object):
            self.add(node, self.meta_model_namespace.type, self.get_element_node(element.type))
            
            #attributes['type'] = self.get_reference(item.type)
            for prop in element.type.attributes.values():
                values = prop._get_values_(element)
                if values:
                    
                    
                    if prop.isUnique and not prop.isOrdered:
                        add_values = self.extend
                    else:
                        # better choice in some cases?
                        add_values = self.extend_with_list
                        
                    if isinstance(prop, self.meta_model.DataProperty):
                        handle_value = lambda value: self.add_data_value(prop.type, value)
                    elif isinstance(prop, self.meta_model.CompositionProperty):
                        handle_value = self.add_element # TODO: check model
                    else:
                        handle_value = self.get_element_node

                    add_values(node, [handle_value(value) for value in values], self.get_element_node(prop))

                        
                    continue
                    
                    match prop.get_meta_class_name():
                        case 'CompositionProperty':
                            child = etree.Element('Components')
                            child.extend(self.item_to_xml(value) for value in values)
                        case 'ReferenceProperty':
                            child = etree.Element('References')
                            child.attrib['refs'] = ' '.join(
                                self.get_reference(value) for value in values)
                        case 'DataProperty':
                            child = etree.Element('Data')
                            child.extend(self.data_to_xml(prop.type, value) for value in values)
                        case _:
                            continue
                        
                   # child.attrib['property'] = prop.name
                   # children.append(child)
                    
        return node
                    
                    
        sorted_attributes = {}
        if name:= attributes.pop('name', None):
            sorted_attributes['name'] = name
        if id_:= attributes.pop('id', None):
            sorted_attributes['id'] = id_
        sorted_attributes.update(sorted(attributes.items()))

        xml = etree.Element(
            item.get_meta_class_name(),
            sorted_attributes)
        xml.extend(children)
        
        self.xml_by_item[item] = xml
        return xml
    
    
    
    
        
        
        
        
        
        
        
        self.meta_model = sys.modules[model.__module__]
        self.model = model
        self.reference_by_model = {model: ''}
        
        self._id_by_element = {}
        self._id_count_by_type_name = {}
        self.xml_by_item = {}
        self.xml = self.item_to_xml(model)

        for element, id_ in self._id_by_element.items():
            xml = self.xml_by_item[element]
            assert 'id' not in xml.attrib
            assert 'name' not in xml.attrib
            attributes = {'id': id_[1:]}
            attributes.update(xml.attrib)
            xml.attrib.clear()
            xml.attrib.update(attributes)

        for ref_model, prefix in self.reference_by_model.items():
            if ref_model in (model, self.meta_model.BUILTIN):
                continue
            self.xml.insert(0, etree.Element(
                'Import',
                source=ref_model.uri,
                prefix=prefix))


    def item_to_xml(self, item):
        attributes = {}
        children = []

        def add_children(members):
            children.extend(self.item_to_xml(member) for member in members)

        if isinstance(item, self.meta_model.NamedElement):
            attributes['name'] = item.name
        if isinstance(item, self.meta_model.Model):
            attributes['uri'] = item.uri
        if isinstance(item, self.meta_model.Package):
            add_children(item.packagedElements)
        if isinstance(item, self.meta_model.Type):
            if item.superTypes:
                st_string = ' '.join(self.get_reference(type_) for type_ in item.superTypes)
                attributes['superTypes'] = st_string
            add_children(item.ownedAttributes)
        if isinstance(item, self.meta_model.Property):
            attributes['type'] = self.get_reference(item.type)
            attributes['lower'] = str(item.lower)
            attributes['upper'] = '*' if item.upper is None else str(item.upper)
            attributes['isOrdered'] = 'true' if item.isOrdered else 'false'
            if not item.get_meta_class_name() == 'CompositionProperty':
                attributes['isUnique'] = 'true' if item.isUnique else 'false'
            if item.get_meta_class_name() == 'ReferenceProperty':
                attributes['oppositeLower'] = str(item.oppositeLower)
                if item.oppositeUpper is None:
                    attributes['oppositeUpper'] = '*'
                else:
                    attributes['oppositeUpper'] = str(item.oppositeUpper)
        if isinstance(item, self.meta_model.Enumeration):
            add_children(item.orderedOwnedLiterals)


        if isinstance(item, self.meta_model.Object):
            attributes['type'] = self.get_reference(item.type)
            for prop in item.type.attributes.values():
                values = prop._get_values_(item)
                if values:
                    match prop.get_meta_class_name():
                        case 'CompositionProperty':
                            child = etree.Element('Components')
                            child.extend(self.item_to_xml(value) for value in values)
                        case 'ReferenceProperty':
                            child = etree.Element('References')
                            child.attrib['refs'] = ' '.join(
                                self.get_reference(value) for value in values)
                        case 'DataProperty':
                            child = etree.Element('Data')
                            child.extend(self.data_to_xml(prop.type, value) for value in values)
                        case _:
                            continue
                        
                    child.attrib['property'] = prop.name
                    children.append(child)
                    
                    
        sorted_attributes = {}
        if name:= attributes.pop('name', None):
            sorted_attributes['name'] = name
        if id_:= attributes.pop('id', None):
            sorted_attributes['id'] = id_
        sorted_attributes.update(sorted(attributes.items()))

        xml = etree.Element(
            item.get_meta_class_name(),
            sorted_attributes)
        xml.extend(children)
        
        self.xml_by_item[item] = xml
        return xml
    
    
    def add_data_value(self, data_type, value):
        if isinstance(value, str):
            return rdflib.Literal(value)

        else:
            raise TypeError(value)


    def get_reference(self, element):
        model, qname = element.get_model_and_qname()
        if qname is None:
            if model is not self.model:
                model, qname = element.get_model_and_qname()
                raise Exception('TODO')
            id_ = self._id_by_element.get(element)
            if id_ is None:
                try:
                    type_name = element.type.name
                except AttributeError:
                    raise # TODO
                nr = self._id_count_by_type_name.get(type_name, 0) + 1
                self._id_count_by_type_name[type_name] = nr
                id_ = f'#{type_name}{nr}'
                self._id_by_element[element] = id_
            return id_
                
            
        else:
            return f'{self.get_model_reference(model)}.{qname}'

    def get_model_reference(self, model):
        reference = self.reference_by_model.get(model)
        if reference is None:
            reference = self._find_free_prefix(model.name)
            self.reference_by_model[model] = reference
        return reference

    def _find_free_prefix(self, prefix):

        def suffixes():
            yield ''
            for nr in itertools.count():
                yield str(nr)
        for suffix in suffixes():
            candidate = prefix + suffix
            if candidate not in self.reference_by_model.values():
                return candidate


class XmlImporter:

    def __init__(self, source, meta_model=None):
        if not meta_model:
            from pnb.mcl.model import standard as meta_model
        self.meta_model = meta_model
        self.item_by_xml_symbol = {}
        root = source

        self._build_packaged_elements(root)
        self.package = self._build_package(root, self.meta_model.Model)

    # def _get_type_infos(self, root_element):
    #     type_infos = []
    #     for xmi_element_tag in ['Class', 'DataType', 'Enumeration', 'PrimitiveType']:
    #         for xmi_element in root_element.xpath(
    #                 f'//*[@xmi:type="uml:{xmi_element_tag}"]', namespaces=NAMESPACES):
    #             xmi_id = xmi_element.attrib[XMI.id]
    #             super_type_xmi_ids = set(xmi_element.xpath(
    #                 f'generalization[@xmi:type="uml:Generalization"]/@general',
    #                 namespaces=NAMESPACES))
    #             type_infos.append(TypeInfo(xmi_id, super_type_xmi_ids, xmi_element))
    #     return list(sorted_by_dependency(type_infos))

    def _build_packaged_elements(self, root_element):
        pass

        #type_infos = self._get_type_infos(root_element)

    def _build(self, element):
        # TODO: mod name for symbols
        xml_symbol = element.attrib.get('name')
        built = self.item_by_xml_symbol.get(xml_symbol)
        if built:
            return built

        xml_tag = element.tag
        match xml_tag:
            case 'Package':
                return self._build_package(element, self.meta_model.Package)
            case 'Model':
                return self._build_package(element, self.meta_model.Model)

    def _build_package(self, package_element, package_class):
        name = package_element.attrib.get('name')
        #TODO: is else part needed?
        if package_class is self.meta_model.Model:
            uri = package_element.attrib.get('uri')
            default_prefix = package_element.attrib.get('defaultPrefix')
            package = package_class(name, uri, default_prefix)
        else:
            package = package_class(name)

        for child_element in package_element:
            built = self._build(child_element)
            # TODO: can built=None happen?
            if built is None:
                #print('######### built=None')
                pass
            elif isinstance(built, self.meta_model.PackageableElement):
                if not isinstance(built, self.meta_model.PrimitiveType):
                    package.packagedElements.add(built)

        return package


def read_xml(source):

    tree = etree.parse(source)
    info = tree.docinfo
    v, e, d = info.xml_version, info.encoding, info.doctype
    print(v, e, d)
    reader = XmlImporter(tree.getroot())
    return reader.package
