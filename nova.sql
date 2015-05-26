/* Instances grouped by image. */
SELECT COUNT(i.image_ref),
       i.image_ref
       FROM instances as i
       GROUP BY i.image_ref
       ORDER BY COUNT(i.image_ref);

/* Running instances grouped by compute node and image. */
SELECT COUNT(i.node),
       i.node,
              i.image_ref
	      FROM instances as i
	      WHERE i.terminated_at IS NULL
	      GROUP BY i.node, i.image_ref
	      ORDER BY COUNT(i.node);

/* Historic VMs grouped by compute node. */
SELECT COUNT(i.node),
       i.node
       FROM instances as i
       GROUP BY i.node
       ORDER BY COUNT(i.node);

/* Current instances grouped by size. */
SELECT COUNT(i.instance_type_id),
       it.name
       FROM instances AS i
       INNER JOIN instance_types AS it ON it.id = i.instance_type_id
       WHERE i.deleted_at IS NULL
       GROUP BY i.instance_type_id;

/*  Current instances grouped by host and size. */
SELECT COUNT(i.instance_type_id),
       it.name,
              i.host
	      FROM instances AS i
	      INNER JOIN instance_types AS it ON it.id = i.instance_type_id
	      WHERE i.deleted_at IS NULL
	      GROUP BY i.host, i.instance_type_id
	      ORDER BY i.host, COUNT(i.instance_type_id) DESC;
